from rest_framework import generics 
from rest_framework import permissions

from .serializers import OrderSerializer 

from .models import Order

from library.permissions import IsOwnerOrLibrarianOrAdmin


class OrderListCreate(generics.ListCreateAPIView):
    """ 
    Order list-create view. Displays current user's orders unless the user 
    has is_superuser=True (if this is the case, then all orders are shown).
    """
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_queryset(self):
        if self.request.user.role == 1 or self.request.user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)
        
    
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    permission_classes = [IsOwnerOrLibrarianOrAdmin, ]
    lookup_field = 'id'