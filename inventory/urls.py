from django.urls import path
from .views import dashboard_view, manager_dashboard_view, custom_login_view, custom_logout_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('manager/', manager_dashboard_view, name='manager_dashboard'),
    path('login/', custom_login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
]