from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
import jwt

from core.models import User


class JWTAuthentication(BaseAuthentication):


    def authenticate(self, request):

        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(" ")

        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed('Token not valid')
    
        token = auth_token[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithm="HS256")

            username = payload['username']

            user = User.objects.get(username=username)

            return (user, token)
        
        except jwt.ExpiredSignatureError as error:
            raise exceptions.AuthenticationFailed('Token is expired. Login again')
        
        except jwt.DecodeError as error:
            raise exceptions.AuthenticationFailed('Token is invalid. Login again')

        except User.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed('No such user')


        