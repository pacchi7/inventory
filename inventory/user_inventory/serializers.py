from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User



class UserSignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'password')

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format.")

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")

        return value

    def create(self, validated_data):
        validated_data['username'] = validated_data['email'] 
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['name'],
            password=validated_data['password']
        )
        return user



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, data):
        import pdb
        pdb.set_trace()
        from django.contrib.auth.hashers import check_password
        user = User.objects.filter(email=data['email']).first()
        if user.email == data['email'] and user.password == data['password']:
            raise serializers.ValidationError("Invalid email or password.")
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'name': user.first_name,
                'email': user.email
            }
        }



from .models import Items
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class GetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['name','description','quantity','price','created_by','updated_by','created_at','updated_at']
