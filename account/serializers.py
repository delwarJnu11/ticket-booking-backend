from rest_framework import serializers
from account.models import UserAccount

class UserSerializer(serializers.ModelSerializer):
#     password=None
    class Meta:
        model = UserAccount
        fields = ['username', 'first_name', 'last_name', 'email','password', 'phone', 'nid', 'address', 'image' ]
        extra_kwargs = {'password': {'write_only': True,}}


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = UserAccount
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'phone', 'nid', 'address', 'image' ]
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        phone = self.validated_data['phone']
        nid = self.validated_data['nid']
        address = self.validated_data['address']
        image = self.validated_data['image']

        if password != confirm_password:
                raise serializers.ValidationError({'error': "Password doesn't matched"})

        if UserAccount.objects.filter(email = email).exists():
                raise serializers.ValidationError({'error': "email already exists"})
        
        account = UserAccount(username = username, first_name = first_name, last_name = last_name, email = email, phone = phone, nid = nid, address= address, image = image)

        account.set_password(password)
        account.is_active = False
        account.balance = 0
        account.save()

        return account
    
class UserLoginSerializer(serializers.Serializer):
     username = serializers.CharField(required=True)
     password = serializers.CharField(required=True)