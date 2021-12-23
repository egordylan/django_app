from django.db import models
from django_app.helpers.models import TrackingModels
from statuses.models import Status
from users.models import User


class Ticket(TrackingModels):
    title = models.CharField(max_length=255)
    desc = models.TextField()  # description
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # status = models.ForeignKey(to=Status,
    #                            limit_choices_to={'is_staff': True},
    #                            on_delete=models.CASCADE)  # передать статус от суппорта? правильно ли сделано вообще?



    def __str__(self):
        return self.title
