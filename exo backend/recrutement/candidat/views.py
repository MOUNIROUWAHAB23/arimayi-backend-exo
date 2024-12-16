from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Candidat, Recruteur
from .serializer import CandidatSerializer, RecruteurSerializer

class CandidatListCreateView(generics.ListCreateAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer

class CandidatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer

class RecruteurListView(generics.ListAPIView):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer

