from xml.dom import ValidationErr

from django.contrib.auth.password_validation import validate_password
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from account.models import CustomerUser
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from account.utils import Util


class RegistrationSerializer(serializers.ModelSerializer, CountryFieldMixin):

    class Meta:
        model = CustomerUser
        fields = (
            'username',
            'full_name',
            'email',
            'password',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number'
        )
class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)
    class Meta:
        model = CustomerUser
        fields = [
            'email',
            'password'
        ]

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = [
            'full_name',
            'email',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number',
        ]

class ChangePasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = ['password']

class EditProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = [
            'full_name',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number',
        ]


    def update(self, instance, validated_data):

        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.country = validated_data.get('country', instance.country)
        instance.company = validated_data.get('company_name', instance.company_name)
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.corporate_number = validated_data.get('corporate_number', instance.corporate_number)
        instance.save()
        return instance

class SendPasswordEmailSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=255)
    class Meta:
        model = CustomerUser
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if CustomerUser.objects.filter(email=email).exists():
            user = CustomerUser.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password reset token', token)
            link = 'http://127.0.0.1:8000/auth/user/reset/'+uid+'/'+token
            print(link)
            body = 'Click following link to reset your password' + link
            data = {
                'subject': 'Reset your password',
                'body': body,
                'to_email': user.email,
            }
            Util.send_email(data)
            return attrs

        else:
            raise ValidationErr('You are not a registered user')

class UserPasswordResetSerializer(serializers.Serializer):

    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    password1 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password1 = attrs.get('password1')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password1:
                raise serializers.ValidationError('Password and confirm password doesnt match')
            id = smart_str(urlsafe_base64_decode(uid))
            user = CustomerUser.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationErr('Token is not valid or expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator(user, token)
            raise ValidationErr('Token is not valid or expired')

