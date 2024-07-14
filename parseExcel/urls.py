# myapp/urls.py
from django.urls import path
from .views import PetListView, PetDetailView

urlpatterns = [
    path('pets/', PetListView.as_view(), name='pet-list'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
]
