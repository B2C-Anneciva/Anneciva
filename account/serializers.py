from rest_framework import serializers
from account.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
            'password2',
            'country',
            'company_name',
            'pc',
            'phone_number',
            'corporate_number'
        )

        def validate(self, args):
            email = args.get('email', None)
            password = args.get('password', None)
            password2 = args.get('password2', None)
            if User.objects.filter(password == password2).exists():
                if User.objects.filter(email=email).exists():
                    raise serializers.ValidationError({'email': ('email already exists')})
                raise serializers.ValidationError({'password': ('Please make sure the password fields is same!')})
            return super().validate(args)

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)