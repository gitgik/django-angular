"""Create views."""
from rest_framework.generics import ListApiView

from .models import Card, List
from .serializers import ListSerializer, CardSerializer


class ListView(ListApiView):
    """ListView."""
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardView(ListApiViesw):
    """CardView."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
