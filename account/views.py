import uuid

from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.models import CustomerUser
from account.serializers import RegistrationSerializer
# @api_view(['POST'])
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
        return Response({'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# class Registration(ModelViewSet):
#
#     # queryset = CustomerUser.objects.all()
#     serializer_class = RegistrationSerializer
#
#     def register(request):
#         print(request.POST)
#         if request.method == 'POST':
#             email = request.POST.get('email', None)
#             username = request.POST.get('username', None)
#             password = request.POST.get('password', None)
#             password2 = request.POST.get('password', None)
#             country = request.POST.get('country', None)
#             company_name = request.POST.get('company_name', None)
#             pc = request.POST.get('pc', None)
#             phone_number = request.POST.get('phone_number', None)
#             corporate_number = request.POST.get('corporate_number', None)
#             user: CustomerUser = CustomerUser.objects.filter(email=email)
#             if user:
#                 user_message = 'This email is busy'
#             elif password2 != password:
#                 password_message = 'Please make sure the password fields is same!'
#             else:
#                 user = CustomerUser.objects.create(
#                     email=email,
#                     username=username,
#                     password=password,
#                     country=country,
#                     phone_number=phone_number,
#                     company_name=company_name,
#                     pc=pc,
#                     corporate_number=corporate_number
#                 )
#                 user.set_password(password)
#                 user.save()
#                 return Response({
#                     'RequestId':str(uuid.uuid4),
#                     'Message': 'User created succesfully',
#                     'User': user.data},
#                     status=status.HTTP_201_CREATED
#                 )
#         return Response({'Errors': user.errors}, status=status.HTTP_400_BAD_REQUEST)

