
from rest_framework import serializers
from .models import Family, Individual, Member, Network, Orb

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ('id', 'title', 'description')


class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = ('id', 'name', 'description')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'description')


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ('id', 'title', 'description')


class OrbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orb
        fields = ('id', 'title', 'description')