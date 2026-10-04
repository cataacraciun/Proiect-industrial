from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Material, Requisition, Department, Equipment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def custom_logout_view(request):
    logout(request)
    return redirect('login')
def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('manager_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'inventory/login.html', {'form': form})

def dashboard_view(request):
    materials = Material.objects.all()
    requisitions = Requisition.objects.all().order_by('-created_at')
    departments = Department.objects.all()
    equipments = Equipment.objects.all()  # Adăugăm echipamentele

    if request.method == 'POST':
        material_id = request.POST.get('material')
        department_id = request.POST.get('department')
        equipment_id = request.POST.get('equipment')
        quantity = request.POST.get('quantity')

        if material_id and department_id and quantity:
            material = Material.objects.get(id=material_id)
            department = Department.objects.get(id=department_id)
            equipment = Equipment.objects.get(id=equipment_id) if equipment_id else None

            Requisition.objects.create(
                material=material,
                department=department,
                equipment=equipment,
                quantity_requested=quantity
            )
            return redirect('dashboard')

    context = {
        'materials': materials,
        'requisitions': requisitions,
        'departments': departments,
        'equipments': equipments,
    }
    return render(request, 'inventory/dashboard.html', context)


@login_required(login_url='login')
def manager_dashboard_view(request):
    error_msg = None
    if request.method == 'POST':
        requisition_id = request.POST.get('requisition_id')
        equipment_id = request.POST.get('equipment_id')
        action = request.POST.get('action')

        try:
            if requisition_id:
                requisition = Requisition.objects.get(id=requisition_id)
                if action == 'approve':
                    requisition.status = 'APPROVED'
                elif action == 'reject':
                    requisition.status = 'REJECTED'
                requisition.save()
            elif equipment_id:
                equipment = Equipment.objects.get(id=equipment_id)
                if equipment.is_running:
                    # Dacă utilajul e pornit, îl oprim și preluăm eroarea introdusă
                    equipment.is_running = False
                    equipment.error_message = request.POST.get('error_message', 'Oprire manuală / Mentenanță')
                else:
                    # Dacă îl repornim, ștergem eroarea
                    equipment.is_running = True
                    equipment.error_message = ""
                equipment.save()
        except Exception as e:
            error_msg = str(e)

        if not error_msg:
            return redirect('manager_dashboard')

    requisitions = Requisition.objects.all().order_by('-created_at')
    equipments = Equipment.objects.all()
    context = {
        'requisitions': requisitions,
        'equipments': equipments,
        'error_message': error_msg,
    }
    return render(request, 'inventory/manager_dashboard.html', context)

    requisitions = Requisition.objects.all().order_by('-created_at')
    equipments = Equipment.objects.all()
    context = {
        'requisitions': requisitions,
        'equipments': equipments,
        'error_message': error_message,
    }
    return render(request, 'inventory/manager_dashboard.html', context)