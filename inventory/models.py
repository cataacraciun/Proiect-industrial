from django.db import models
from django.core.exceptions import ValidationError


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nume Departament")

    def __str__(self):
        return self.name


class Equipment(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Cod Utilaj / Linie")
    name = models.CharField(max_length=150, verbose_name="Denumire Echipament")
    location = models.CharField(max_length=100, verbose_name="Locație / Hală")
    is_running = models.BooleanField(default=True, verbose_name="Utilaj Pornit / Funcțional")
    error_message = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cod / Descriere Eroare PLC")

    def __str__(self):
        status = "Pornit" if self.is_running else f"Oprit (Eroare: {self.error_message or 'Mentenanță'})"
        return f"{self.code} - {self.name} [{status}]"


class Material(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Cod Structură / Piese")
    name = models.CharField(max_length=150, verbose_name="Denumire Material")
    stock_quantity = models.IntegerField(default=0, verbose_name="Stoc Curent")
    minimum_limit = models.IntegerField(default=5, verbose_name="Prag Minim Alertă")

    def __str__(self):
        return f"{self.code} - {self.name}"


class Requisition(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'În așteptare'),
        ('APPROVED', 'Aprobată'),
        ('REJECTED', 'Respinsă'),
    ]

    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Material Cerut")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Departament Solicitant")
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name="Utilaj / Echipament Defect")
    quantity_requested = models.IntegerField(verbose_name="Cantitate Cerută")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING', verbose_name="Status Cerere")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data Creării")

    def save(self, *args, **kwargs):
        if self.pk:
            original = Requisition.objects.get(pk=self.pk)
            if self.status == 'APPROVED' and original.status != 'APPROVED':
                if self.material.stock_quantity >= self.quantity_requested:
                    self.material.stock_quantity -= self.quantity_requested
                    self.material.save()
                else:
                    raise ValidationError("Stoc insuficient în inventar pentru a aproba această cerere!")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Cerere #{self.id} - {self.material.name} ({self.quantity_requested} buc)"