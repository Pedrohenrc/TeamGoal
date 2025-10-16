from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login
from django.contrib.auth import get_user_model

User = get_user_model()

class HomeView(TemplateView):
    """Landing page inicial"""
    template_name = 'home.html'

@receiver(pre_social_login)
def link_to_existing_user(sender, request, sociallogin, **kwargs):
    if sociallogin.is_existing:
        return
    
    email = sociallogin.account.extra_data.get('email', '')
    
    try:
        user = User.objects.get(email=email)
        sociallogin.connect(request, user)
    except User.DoesNotExist:
        pass
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = 'core:home'  # Redireciona para home se não logado
    
    # Só usuários autenticados podem acessar
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)
    
