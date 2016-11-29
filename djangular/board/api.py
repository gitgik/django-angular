"""Create views."""
from rest_framework.generics import ListAPIView

from .models import Card, List
from .serializers import ListSerializer, CardSerializer


class ListView(ListAPIView):
    """ListView."""
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardView(ListAPIView):
    """CardView."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
