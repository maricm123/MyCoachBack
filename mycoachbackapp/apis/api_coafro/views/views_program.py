from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import permissions
from django.shortcuts import get_object_or_404  
from ..serializers.serializers_program import ProgramSerializer, CategorySerializer
from profiles.models.coach import Coach
from profiles.models.user import User
from rest_framework.decorators import api_view, permission_classes
from trainingProgram.models.program import Program
from trainingProgram.models.category import Category
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

""" https://www.django-rest-framework.org/api-guide/generic-views/ """


class ProgramView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get_queryset(self):
        return Program.objects.all()

    def get(self, request):
        programs = Program.objects.all()
        serializer = ProgramSerializer(programs, many=True)

        serialized_data = serializer.data
        return Response(serialized_data, status = HTTP_200_OK)

class ProgramDetail(RetrieveAPIView):
    """ Get one program with provided id (With retrieve APIView)"""
    serializer_class = ProgramSerializer
    lookup_field='id'
    queryset = Program.objects.all()


class CoachProgramView(ListCreateAPIView):
    """ List all programs of coach """
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        programs = Program.objects.filter(coach__user=self.request.user.id)
        serializer = ProgramSerializer(programs, many=True)
        
        serialized_data = serializer.data
        return Response(serialized_data, status = HTTP_200_OK)

    # def get_queryset(self):
    #     print(self.queryset.filter(coach__user=self.request.user.id))
    #     return self.queryset.filter(coach__user=self.request.user.id)

    def perform_create(self, serializer):
        print(self.request.data)
        category = Category.objects.get(id=self.request.data["category.category"])
        # category = Category.objects.get(id=)
        print(category)
        coach = Coach.objects.get(user_id=self.request.user.id)
        obj = serializer.save(coach=coach, category=category)
        # obj.category.add(category)
        obj.save()
        

 
class CoachProgramDetail(APIView):
    """ Get one program of coach with provided id (With APIView)"""
    permission_classes = (permissions.AllowAny,)

    def get_object(self, id):
        try:
            return Program.objects.get(id=id)
        except Program.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):
        program = self.get_object(id)
        serializer = ProgramSerializer(program)
        return Response(serializer.data)

    # Updating program
    def put(self, request, id, format=None):
        program = self.get_object(id)
        serializer = ProgramSerializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CoachProgramUpdateView(RetrieveUpdateAPIView):
#     queryset = Program.objects.all()
#     serializer_class = ProgramSerializer



@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def delete_program(request, program_id):
    program = Program.objects.filter(pk=program_id)
    program.delete()

    return Response({'message': 'The program was deleted'})

class CategoryView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)

        serialized_data = serializer.data
        return Response(serialized_data, status = HTTP_200_OK)

