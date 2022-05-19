from rest_framework import serializers
from account.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','is_verified']
        
class VerifyAccountSerializer(serializers.Serializer):
    email=serializers.EmailField()
    otp=serializers.CharField()
         
class DetailAccountSerializer(serializers.Serializer):
    age=serializers.IntegerField()
    email=serializers.EmailField()
    otp=serializers.CharField()
    class Meta:
        model=User
        fields=['email','age','otp']
         
           