from django.shortcuts import render
from rest_framework import viewsets
from .models import Family, Individual, Member, Network, Orb
from .serializers import FamilySerializer, IndividualSerializer, MemberSerializer, NetworkSerializer, OrbSerializer


class FamilyView(viewsets.ModelViewSet):
      serializer_class = FamilySerializer
      queryset = Family.objects.all()


class IndividualView(viewsets.ModelViewSet):
      serializer_class = FamilySerializer
      queryset = Individual.objects.all()


class MemberView(viewsets.ModelViewSet):
      serializer_class = FamilySerializer
      queryset = Member.objects.all()


class NetworkView(viewsets.ModelViewSet):
      serializer_class = NetworkSerializer
      queryset = Network.objects.all()


class OrbView(viewsets.ModelViewSet):
      serializer_class = OrbSerializer
      queryset = Orb.objects.all()