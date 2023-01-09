import uuid

from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.response import Response

from account.models import User
from account.serializers import RegistrationSerializer

class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                'RequestId':str(uuid.uuid4),
                'Message': 'User created succesfully',
                'User': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response({'Errors': serializers.errors}, status=status.HTTP_400_BAD_REQUEST)

