from rest_framework import serializers
from account.models import UserAccount
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
#     password=None
    class Meta:
        model = UserAccount
        fields = ['id','username', 'first_name', 'last_name', 'email','password', 'phone', 'nid', 'address', 'image' ]
        extra_kwargs = {'password': {'write_only': True,}}


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = UserAccount
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'phone', 'nid', 'address', 'image']
        extra_kwargs = {
            'password': {'write_only': True, 'validators': [validate_password]},
        }

    def validate_email(self, value):
        if UserAccount.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password from the data before creating the user
        user = UserAccount.objects.create_user(**validated_data)
        user.is_active = False
        user.balance = 0
        user.save()
        return user
    
class UserLoginSerializer(serializers.Serializer):
     username = serializers.CharField(required=True)
     password = serializers.CharField(required=True)