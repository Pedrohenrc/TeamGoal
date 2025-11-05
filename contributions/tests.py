
import pytest
from contributions.models import Contribution
from subgoals.models import SubGoal
from goals.models import Goal
from teams.models import Team

@pytest.mark.django_db
class TestContributionViewSet:
    
    def test_listar_contributions(self, usuario_logado):
        """Testa listar contributions"""
        api_client, usuario = usuario_logado
        
        response = api_client.get('/api/contributions/')
        assert response.status_code == 200
    
    def test_stats_contributions(self, usuario_logado):
        """Testa retornar estatísticas"""
        api_client, usuario = usuario_logado
        
        response = api_client.get('/api/contributions/stats/')
        assert response.status_code == 200
        assert 'total_contributions' in response.data
        assert 'total_progress' in response.data