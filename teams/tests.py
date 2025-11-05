import pytest
from teams.models import Team
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestTeamViewSet:
    
    def test_listar_times_sem_autenticacao(self, api_client):
        """Testa se retorna 401 sem autenticação"""
        response = api_client.get('/api/teams/')
        assert response.status_code == 401
    
    def test_listar_times_com_autenticacao(self, usuario_logado):
        """Testa se lista times do usuário"""
        api_client, usuario = usuario_logado
        response = api_client.get('/api/teams/')
        assert response.status_code == 200
        assert 'results' in response.data or isinstance(response.data, list)
    
    def test_criar_time(self, usuario_logado):
        """Testa criar um novo time"""
        api_client, usuario = usuario_logado
        data = {
            'name': 'Time Teste',
            'description': 'Descrição teste'
        }
        response = api_client.post('/api/teams/', data, format='json')
        assert response.status_code == 201
        assert response.data['name'] == 'Time Teste'
        assert response.data['owner'] == usuario.id
    
    def test_adicionar_membro(self, usuario_logado):
        """Testa adicionar membro ao time"""
        api_client, owner = usuario_logado
        
        # Cria time
        team = Team.objects.create(name='Time A', owner=owner)
        
        # Cria outro usuário
        outro_user = User.objects.create_user(username='outro', password='123')
        
        # Tenta adicionar
        response = api_client.post(
            f'/api/teams/{team.id}/add-member/',
            {'user_id': outro_user.id},
            format='json'
        )
        assert response.status_code == 200
        assert outro_user in team.members.all()
    
    def test_remover_membro(self, usuario_logado):
        """Testa remover membro do time"""
        api_client, owner = usuario_logado
        
        # Cria time e adiciona membro
        outro_user = User.objects.create_user(username='outro', password='123')
        team = Team.objects.create(name='Time A', owner=owner)
        team.members.add(outro_user)
        
        # Remove
        response = api_client.post(
            f'/api/teams/{team.id}/remove-member/',
            {'user_id': outro_user.id},
            format='json'
        )
        assert response.status_code == 200
        assert outro_user not in team.members.all()