from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tickets.serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated
from tickets.models import Ticket


class TicketsAPIView(ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Ticket.objects.filter(owner=self.request.user)


class TicketDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Ticket.objects.filter(owner=self.request.user)


    
