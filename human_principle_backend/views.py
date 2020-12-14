from django.shortcuts import render
from rest_framework import viewsets
from .models import Member, Principle
from .serializers import MemberSerializer, PrincipleSerializer
from rest_framework.permissions import IsAuthenticated


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class PrincipleViewSet(viewsets.ModelViewSet):
    queryset = Principle.objects.all()
    serializer_class = PrincipleSerializer
    permission_classes = [IsAuthenticated]
