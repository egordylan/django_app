from django.db import models
from django_app.helpers.models import TrackingModels
from users.models import User


class Ticket(TrackingModels):
    title = models.CharField(max_length=255)
    desc = models.TextField()  # description
    #is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)  # передать статус от суппорта

    def __str__(self):
        return self.title

