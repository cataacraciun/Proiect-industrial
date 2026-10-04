from django.test import TestCase
from .models import Material, Department, Requisition


class RequisitionAutomationTestCase(TestCase):

    def setUp(self):
        # Pregătim datele de test înainte de rulare
        self.department = Department.objects.create(name="Dispecerat")
        self.material = Material.objects.create(
            code="GEN-TEST",
            name="Cablaj Test",
            stock_quantity=10,
            minimum_limit=2
        )

    def test_stock_decreases_when_approved(self):
        # 1. Cream o cerere nouă (în status 'PENDING')
        requisition = Requisition.objects.create(
            material=self.material,
            department=self.department,
            quantity_requested=4
        )

        # Stocul inițial trebuie să fie tot 10, pentru că e doar în așteptare
        self.material.refresh_from_db()
        self.assertEqual(self.material.stock_quantity, 10)

        # 2. Schimbăm statusul cererii în 'APPROVED'
        requisition.status = 'APPROVED'
        requisition.save()

        # 3. Verificăm dacă stocul a scăzut automat (10 - 4 = 6)
        self.material.refresh_from_db()
        self.assertEqual(self.material.stock_quantity, 6)