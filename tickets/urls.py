from django.urls import path
from tickets.views import TicketsAPIView, TicketDetailAPIView


urlpatterns = [
    path('', TicketsAPIView.as_view(), name='tickets'),
    path('<int:id>', TicketDetailAPIView.as_view(), name='ticket'),
]
