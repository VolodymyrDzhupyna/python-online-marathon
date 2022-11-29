from rest_framework import generics  
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 

from .models import CustomUser 
from order.models import Order
from .serializers import CustomUserSerializer 
from order.serializers import OrderSerializer 

from library.permissions import IsLibrarianOrAdmin, IsSelfOrReadOnly


class UserListCreate(generics.ListCreateAPIView):
    """
    Generic list-create API endpoint. Create operations are only allowed to 
    authenticated users.
    """
    serializer_class = CustomUserSerializer 
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = CustomUser.objects.all()
           
           
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """ 
    Generic retrieve-update-destroy API endpoint. Combinated with the previous view,
    it gives full CRUD functionality to the User model. 
    """
    
    serializer_class = CustomUserSerializer 
    permission_classes = [IsSelfOrReadOnly, ]
    queryset = CustomUser.objects.all()
    lookup_field = 'id'
    
    
class UserOrders(APIView):
    
    permission_classes = [IsLibrarianOrAdmin, ]
    """ 
    Searches orders for the specific user. With no `order_id` specified, returns 
    all orders associated with the given user.
    """
    
    def get(self, request, user_id, order_id=''):
        
        user_obj = CustomUser.get_by_id(user_id)
        if user_obj:
            if order_id:
                order_obj = Order.get_by_id(order_id)
                if order_obj and order_obj in user_obj.order_set.all():
                    serializer = OrderSerializer(order_obj)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({
                        'Error': 'No order with the given ID found.'
                    }, status=status.HTTP_404_NOT_FOUND)
            else:
                user_orders = user_obj.order_set.all()
                serializer = OrderSerializer(user_orders, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({
                'Error': 'No user with the given ID found'
            }, status=status.HTTP_404_NOT_FOUND)
            