from django.db import models
from django_app.helpers.models import TrackingModels
from tickets.models import Ticket


class Message(TrackingModels):
    ticket_id = models.ForeignKey(to=Ticket, on_delete=models.DO_NOTHING)  # привязать к конкретной графе id у тикета
    parent_id = models.CharField()  # номер сообщения на которое отвечаем, КАК СДЕЛАТЬ
    text = models.TextField()
