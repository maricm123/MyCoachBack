from rest_framework import serializers

from trainingProgram.models.program import Program
from trainingProgram.models.category import Category
from .serializers_profiles import CoachSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    coach = CoachSerializer(read_only=True)

    class Meta:
        model = Program
        fields = ['id', 'name', 'price', 'category', 'coach', 'date_created', 'modified_at']
        read_only_fields = (
            'coach',
            'date_created',
            'modified_at'
        )
