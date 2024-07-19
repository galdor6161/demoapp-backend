from django.urls import path
from .views import get_data, get_more_data

urlpatterns = [
    path('data/', get_data),
    path('moredata/', get_more_data),
]