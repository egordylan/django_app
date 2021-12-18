from rest_framework.serializers import ModelSerializer
from tickets.models import Ticket


class TicketSerializer(ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('id', 'title', 'desc', 'is_complete',)
