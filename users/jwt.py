from rest_framework.authentication import get_authorization_header, \
    BaseAuthentication
from rest_framework import exceptions
import jwt
from django.conf import settings
from users.models import User
from django.core.exceptions import ObjectDoesNotExist


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        # autherization
        auth_header = get_authorization_header(request)

        auth_data = auth_header.decode('utf-8')

        auth_token = auth_data.split(' ')

        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed('Token not valid')

        token = auth_token[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')

            username = payload['username']

            user = User.objects.get(username=username)

            return (user, token)

        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed(
                'Token is expired, login again')

        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed(
                'Token is invalid')

        # Unresolved attribute reference 'DoesNotExist' for class 'User'
        # ШТА? еще не нашла как и откуда его взять. нашла такое
        # https://stackoverflow.com/questions/52455835/where-do-i-import-the-doesnotexist-exception-in-django-1-10-from
        # но это, по идее, тоже самое что и тут написано
        except User.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed(
                'No such user')
        #  This code is unreachable
        #  Why? How to make it reachable?
        return super().authenticate(request)
