from ..serializers.serializers_profiles import CoachSingUpSerializer, ClientSingUpSerializer, CoachLoginSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import AllowAny

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


class CoachLoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CoachLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            # 'token' : serializer.data['token'],
        }

        status_code = status.HTTP_200_OK

        return Response(response, status = status_code)