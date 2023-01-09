from rest_framework import serializers
from account.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'password',
            'country',
            'company_name',
            'pc',
            'phone_number',
            'corporate_number'
        )

        def validate(self, args):
            email = args.get('email', None)
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError('email already exists')
                return super().validate(args)

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)