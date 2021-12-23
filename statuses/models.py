from django.db import models
from django_app.helpers.models import TrackingModels

PENDING = 'Pending'  # не решенные тикеты
DONE = 'Done'  # решенные тикеты
FROZEN = 'Frozen'  # замороженные

STATUSES_OF_TICKETS = [
    (PENDING, 'Pending'),
    (DONE, 'Done'),
    (FROZEN, 'Frozen'),
]


class Status(TrackingModels):
    status_name = models.CharField(max_length=20,
                                   choices=STATUSES_OF_TICKETS,
                                   default=PENDING)
    # who_changed_status = ...
    # id_of_ticket = ... (id тикета к которому приписывается конкретный статус
    def __str__(self):
        return self.status_name
