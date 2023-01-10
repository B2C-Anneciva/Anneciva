from rest_framework import serializers
from account.models import CustomerUser

class RegistrationSerializer(serializers.ModelSerializer):

    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
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
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def validate(self, request, args):
            email = args.get('email', None)
            if CustomerUser.objects.filter(email=email).exists():
                raise serializers.ValidationError({'email': ('email already exists')})
            return super().validate(args)

        def create(self, validated_data):
            return CustomerUser.objects.create_user(**validated_data)