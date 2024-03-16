from rest_framework import serializers
from .models import User, CompanyModel


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'company_name', 'email','password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        company_name = self.validated_data['company_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']


        if password!=password2:
            raise serializers.ValidationError("Password Doesn't Matched!")
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        

        account = User(username = username, first_name = first_name, last_name = last_name, company_name=company_name, email=email)
        account.set_password(password)
        account.is_active = False
        account.save()
        
        CompanyModel.objects.create(
            user= account,
            registered_no = 100+account.id
        )

        return account
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)