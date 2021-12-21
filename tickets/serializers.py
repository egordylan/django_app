from rest_framework.serializers import ModelSerializer
from tickets.models import Ticket
from rest_framework import fields


class TicketSerializer(ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('id', 'title', 'desc', 'is_complete',)
