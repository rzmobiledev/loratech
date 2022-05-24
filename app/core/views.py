from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer, LoginSerializer


"""
This is Endpoint 1 to welcome a user if 
he/she passes the authorization. This endpoint 
will welcome him/her with a plain text
"""
class AuthUserAPIView(GenericAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        # user = request.user
        # serializer = RegisterSerializer(user)
        return Response({'user': 'Hello, you are authorized'})

class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



"""
This is only for testing purpose and not being used
inside api endpoint
"""
class LoginAPIView(GenericAPIView):
    
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        if user:
            serializers = self.serializer_class(user)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        return Response({'message': 'Invalid credential, try again!'}, status=status.HTTP_401_UNAUTHORIZED)
