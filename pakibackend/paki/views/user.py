import json

from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import authentication, permissions
from django.http import HttpResponse, JsonResponse

from ..models import User
from ..serializers.plainserializer import GeneralObjectSerializer
from ..transferobjects.userdata import UserDto


class UserAddView(APIView):
    '''
    API Request to add users
    '''

    parser_classes = [JSONParser]

    def post(self, request, format = None):
        '''
        Get properties of user
        '''
        user = request.data
        try:
            new_user = User(firstName=user['firstname'], lastName=user['lastname'], email=user['email'], latitude=user['latitude'], longitude=user['longitude'])
            new_user.save()
            return Response({'request': 'user_add', 'success': True, 'response': {'user_id': new_user.id}})
        except Exception as inst:
            print(inst)
            return Response({'request': 'user_add', 'success': False, 'response': {}})


class UserGetView(APIView):
    '''
    API Request to get user
    '''

    parser_classes = [JSONParser]

    def get(self, request, format = None, *args, **kwargs):
        '''
        Get properties of user
        '''

        user_email = str(kwargs['email'])

        try:
            requested_user = User.objects.get(email=user_email)

            if requested_user is not None:
                user_dto = UserDto()
                user_dto.first_name = requested_user.firstName
                user_dto.last_name = requested_user.lastName
                user_dto.email_address = requested_user.email
                user_dto.latitude = requested_user.latitude
                user_dto.longitude = requested_user.longitude
                serializer = GeneralObjectSerializer(user_dto)
                serialized = serializer.data
                return JsonResponse(serialized)
            else:
                return Response({'request': 'user_get', 'success': False, 'response': {}})
        except Exception as inst:
            print(inst)
            return Response({'request': 'user_get', 'success': False, 'response': {}})