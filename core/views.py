from django.views.generic import TemplateView
from django.shortcuts import redirect

class HomeView(TemplateView):
    """Landing page inicial"""
    template_name = 'home.html'

# Views temporárias de login
class GoogleLoginView(TemplateView):
    def get(self, request):
        # TODO: Implementar OAuth do Google
        return redirect('core:home')

class GitHubLoginView(TemplateView):
    def get(self, request):
        # TODO: Implementar OAuth do GitHub
        return redirect('core:home')
    
class DashboardView(TemplateView):
    """Dashboard do usuário após login"""
    template_name = 'dashboard.html'
    
    # Só usuários autenticados podem acessar
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
