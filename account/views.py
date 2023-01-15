from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from account.models import CustomerUser
from account.serializers import UserLoginSerializer, RegistrationSerializer
from account.renderers import UserRenderer


class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        data = request.data
        username = data['username']
        full_name = data['full_name']
        email = data['email']
        password = data['password']
        # password1 = data['password1']
        country = data['country']
        company_name = data['company_name']
        user_type = data['user_type']
        phone_number = data['phone_number']
        corporate_number = data['corporate_number']

        if CustomerUser.objects.filter(email=email).exists():
            return Response({'Error': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        # elif password != password:
        #     return Response({'Error': 'Passwords arent match'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = CustomerUser.objects.create_user(
                username=username,
                full_name=full_name,
                email=email,
                password=password,
                country=country,
                company_name=company_name,
                user_type=user_type,
                phone_number=phone_number,
                corporate_number=corporate_number
            )
            user.set_password(password)
            user.save()
            return Response({
                'Message': 'User created succesfully'},
                status=status.HTTP_201_CREATED
            )

class UserLoginView(generics.GenericAPIView):

    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'head', 'post']
    # renderer_classes = [UserRenderer]
    def post(self, request):
        self.http_method_names.append("GET")
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({'Message':'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'Errors': {'non_field_errors': ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)




