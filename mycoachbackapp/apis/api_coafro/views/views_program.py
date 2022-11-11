from rest_framework import viewsets
from django.shortcuts import render
from ..serializers.serializers_program import ProgramSerializer, CategorySerializer

from trainingProgram.models.program import Program
from trainingProgram.models.category import Category

# Samo za listu svih programa
class ProgramView(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()

    def get_queryset(self):
        return self.queryset
        # kada budem hteo da izlistam samo coachove planove kod njega na profilu
        # return self.queryset.filter(created_by=request.user)
    