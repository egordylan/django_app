from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from tickets.serializers import TicketSerializer
from rest_framework import permissions, filters
from rest_framework.permissions import IsAuthenticated
from tickets.models import Ticket
from tickets.pagination import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework.backends import DjangoFilterBackend


class TicketsAPIView(ListCreateAPIView):
    serializer_class = TicketSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]

    filter_set_fields = ['id', 'title', 'desc', 'is_complete']
    search_fields = ['id', 'title', 'desc', 'is_complete']
    ordering_fields = ['id', 'title', 'desc', 'is_complete']

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
