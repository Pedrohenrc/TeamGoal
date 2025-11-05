# contributions/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, Sum, Avg
from contributions.models import Contribution
from .serializers import ContributionSerializer

class ContributionViewSet(viewsets.ModelViewSet):
    serializer_class = ContributionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Contribution.objects.filter(
            Q(goal__team__owner=user) | Q(goal__team__members=user)
        ).distinct()
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        contributions = self.get_queryset()
        
        total_contributions = contributions.count()
        total_progress = contributions.aggregate(total=Sum('progress'))['total'] or 0
        average_progress = contributions.aggregate(avg=Avg('progress'))['avg'] or 0
        
        stats_data = {
            'total_contributions': total_contributions,
            'total_progress': total_progress,
            'average_progress': round(average_progress, 2),
        }
        
        return Response(stats_data, status=status.HTTP_200_OK)