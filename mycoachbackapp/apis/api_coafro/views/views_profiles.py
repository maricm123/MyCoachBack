from ..serializers.serializers_profiles import CoachSingUpSerializer, ClientSingUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request


class ClientSignUpView(generics.GenericAPIView):
    serializer_class = ClientSingUpSerializer

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "Client Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CoachSignUpView(generics.GenericAPIView):
    serializer_class = CoachSingUpSerializer

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "Coach Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
