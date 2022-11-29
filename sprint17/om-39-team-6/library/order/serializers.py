from rest_framework import serializers 

from .models import Order 
from authentication.serializers import CustomUserSerializer


class OrderSerializer(serializers.ModelSerializer):
    
    ordered_book = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Order 
        fields = ('id', 'book', 'user', 'ordered_book', 'created_at', 'end_at',
                  'plated_end_at')
        extra_kwargs = {
            'book': {'write_only': True}
        }
        
    def get_ordered_book(self, obj):
        return f"{obj.book.name} (id={obj.book.id})"
    
    def get_user(self, obj):
        return f"{obj.user.email} (id={obj.user.id})"