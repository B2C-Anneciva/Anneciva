from rest_framework import serializers
from account.models import CustomerUser

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = (
            'email',
            'username',
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
        fields = ['email', 'password']

