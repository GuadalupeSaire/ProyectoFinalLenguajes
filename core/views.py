from django.shortcuts import render
from django.views import View


class LoginVista(View):
    template_name = 'core/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class RegistroVista(View):
    template_name = 'core/registro.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class DashboardVista(View):
    template_name = 'core/dashboard.html'

    def get(self, request):
        return render(request, self.template_name)



class UsuariosVista(View):
    template_name = 'core/usuarios.html'

    def get(self, request):
        usuarios = [
            {
                'nombre': 'Guadalupe',
                'apellidos': 'Saire Flores',
                'telefono': '987654321',
                'correo': 'guadalupe.saire@email.com',
                'membresia': 'Premium',
            },
            {
                'nombre': 'Graciela',
                'apellidos': 'Canales Palomino',
                'telefono': '912345678',
                'correo': 'graciela.canales@email.com',
                'membresia': 'Básico',
            },
        ]
        return render(request, self.template_name, {'usuarios': usuarios})


class LoginEntrenadorVista(View):
    template_name = 'core/login_entrenador.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)




class PlanEntrenamientoVista(View):
    template_name = 'core/plan_entrenamiento.html'

    def contexto(self):
        return {
            'clientes': [
                'Guadalupe Saire Flores',
                'Carlos Fernández',
                'María López',
            ],
            'programas': [
                'Programa de Fuerza',
                'Programa de Resistencia',
                'Programa de Pérdida de Peso',
                'Programa de Flexibilidad',
            ],
        }

    def get(self, request):
        return render(request, self.template_name, self.contexto())

    def post(self, request):
        datos = self.contexto()
        datos['mensaje'] = 'Plan asignado correctamente.'
        return render(request, self.template_name, datos)



class ProgresoVista(View):
    template_name = 'core/progreso.html'

    def contexto(self):
        return {
            'registros': [
                {
                    'nombre': 'Jorge Montes',
                    'fecha': '2026-11-02',
                    'peso': 50,
                    'repeticiones': 12,
                    'comentario': 'Buen progreso esta semana',
                },
                {
                    'nombre': 'Luciana Palomino',
                    'fecha': '2026-11-03',
                    'peso': 70,
                    'repeticiones': 10,
                    'comentario': 'Mejorar técnica',
                },
                {
                    'nombre': 'Dayana Saire',
                    'fecha': '2026-11-04',
                    'peso': 30,
                    'repeticiones': 15,
                    'comentario': 'Incrementar peso la próxima sesión',
                },
            ],
            'clientes': ['Jorge Montes', 'Luciana Palomino', 'Dayana Saire'],
        }

    def get(self, request):
        return render(request, self.template_name, self.contexto())

    def post(self, request):
        datos = self.contexto()
        datos['mensaje'] = 'Progreso registrado correctamente.'
        return render(request, self.template_name, datos)