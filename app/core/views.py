from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer, LoginSerializer


class AuthUserAPIView(GenericAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response({'user':serializer.data})

class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        encrypted = make_password(password)
        check = check_password(password, encrypted)
        user = authenticate(email=email, password=check)
        print(check)

        if user:
            serializers = self.serializer_class(user)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        return Response({'message': 'Invalid credential, try again!'}, status=status.HTTP_401_UNAUTHORIZED)
