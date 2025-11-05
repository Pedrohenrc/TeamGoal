import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.fixture
def api_client():
    """Cliente API pra fazer requisições"""
    return APIClient()

@pytest.fixture
def usuario_teste():
    """Cria um usuário de teste"""
    user = User.objects.create_user(
        username='testuser',
        password='testpass123',
        email='test@test.com'
    )
    return user

@pytest.fixture
def usuario_logado(api_client, usuario_teste):
    """Retorna cliente API com usuário logado"""
    api_client.force_authenticate(user=usuario_teste)
    return api_client, usuario_teste