from rest_framework import serializers
from account.models import CustomerUser

class RegistrationSerializer(serializers.ModelSerializer):

    # password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
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
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

        def validate(self, request, args):
            email = args.get('email', None)
            # password = args.get('password')
            # password2 = args.get('password2')
            if CustomerUser.objects.filter(email=email).exists():
                raise serializers.ValidationError({'email': ('email already exists')})
                # if password != password2:
                #     raise serializers.ValidationError('Passwords arent match')
            return super().validate(args)

        def create(self, validated_data):
            CustomerUser.set_password(validated_data=['password'])
            return CustomerUser.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = CustomerUser
        fields = ['email', 'password']