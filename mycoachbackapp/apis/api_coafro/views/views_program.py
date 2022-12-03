from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import permissions
from ..serializers.serializers_program import ProgramSerializer, CategorySerializer
from profiles.models.coach import Coach
from profiles.models.user import User
from trainingProgram.models.program import Program
from trainingProgram.models.category import Category

# Samo za listu svih programa
class ProgramView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()

    def get_queryset(self):
        return self.queryset


# za izlistavanje programa od coacha
class CoachProgramView(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()

    def get_queryset(self):
        return self.queryset.filter(coach__user=self.request.user.id)
    
    # za kreiranje programa
    def perform_create(self, serializer):
        serializer.save(coach__user=self.request.user.id)