from django.urls import path
from .views import TicketList, TicketDetail, create_ticket

urlpatterns = [
    path('', TicketList.as_view(), name='tickets'),
    path('ticket/<int:pk>/', TicketDetail.as_view(), name='ticket'),
    path('create/', create_ticket, name='create_ticket'),
]