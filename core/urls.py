from django.urls import path
from .views import (
    LoginVista, RegistroVista, DashboardVista,
    UsuariosVista, LoginEntrenadorVista,
    PlanEntrenamientoVista, ProgresoVista,
)

urlpatterns = [
    path('', LoginVista.as_view(), name='login'),
    path('registro/', RegistroVista.as_view(), name='registro'),
    path('dashboard/', DashboardVista.as_view(), name='dashboard'),
    path('usuarios/', UsuariosVista.as_view(), name='usuarios'),
    path('entrenador/', LoginEntrenadorVista.as_view(), name='login_entrenador'),
    path('plan-entrenamiento/', PlanEntrenamientoVista.as_view(), name='plan_entrenamiento'),
    path('progreso/', ProgresoVista.as_view(), name='progreso'),
]