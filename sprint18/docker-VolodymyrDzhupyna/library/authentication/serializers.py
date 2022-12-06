from rest_framework import serializers 

from .models import CustomUser 


class CustomUserSerializer(serializers.ModelSerializer):
    
    role = serializers.SerializerMethodField()
    
    class Meta:
        model = CustomUser 
        fields = ('id', 'email', 'first_name', 'last_name', 'middle_name', 'role',
                  'password')
        extra_kwargs = {
            "password": {"write_only": True}
        }
        
    def get_role(self, obj):
        return obj.get_role_display()
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)