from rest_framework import serializers
from account.models import CustomerUser

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = (
            'email',
            'username',
            'password',
            # 'password2',
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
        fields = ['email', 'password']

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = CustomerUser
        fields = (
            'email',
            'username',
            'password',
            'password1',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }