
import pytest
from goals.models import Goal
from teams.models import Team
from datetime import datetime, timedelta

@pytest.mark.django_db
class TestGoalViewSet:
    
    def test_criar_goal(self, usuario_logado):
        """Testa criar uma meta"""
        api_client, usuario = usuario_logado
        
        # Cria time primeiro
        team = Team.objects.create(name='Time A', owner=usuario)
        
        data = {
            'team': team.id,
            'title': 'Meta 1',
            'description': 'Descrição',
            'deadline': '2025-12-31',
            'status': 'pending'
        }
        response = api_client.post('/api/goals/', data, format='json')
        assert response.status_code == 201
        assert response.data['title'] == 'Meta 1'
    
    def test_listar_goals(self, usuario_logado):
        """Testa listar metas"""
        api_client, usuario = usuario_logado
        
        team = Team.objects.create(name='Time A', owner=usuario)
        Goal.objects.create(
            team=team,
            title='Meta 1',
            description='Desc',
            deadline='2025-12-31'
        )
        
        response = api_client.get('/api/goals/')
        assert response.status_code == 200