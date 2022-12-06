from rest_framework import permissions 

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsLibrarianOrAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        return bool(
            request.user.role == 1 or 
            request.user.is_staff
        )
        

class IsLibrarianOrAdminOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try:
            return bool(
                request.user.role == 1 or 
                request.user.is_superuser
            )
        except AttributeError:
            return bool(
                request.method in SAFE_METHODS
            )
            

        
class IsOwnerOrLibrarianOrAdmin(permissions.BasePermission):
    """Permission which checks if the current user is the user the order is 
    associated with, and, if so, allows altering it."""
    
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_authenticated and 
            request.user == obj.user or
            request.user.role == 1 or 
            request.user.is_superuser
        )
        
        
class IsSelfOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or 
            request.user == obj
        )
