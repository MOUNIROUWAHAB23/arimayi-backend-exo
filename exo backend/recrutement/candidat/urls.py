from django.urls import path
from .views import CandidatListCreateView, CandidatDetailView, RecruteurListView

urlpatterns = [
    path('candidats/', CandidatListCreateView.as_view(), name='candidat-list-create'),
    path('candidats/<int:pk>/', CandidatDetailView.as_view(), name='candidat-detail'),
    path('recruteurs/', RecruteurListView.as_view(), name='recruteur-list'),
]
