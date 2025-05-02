from rest_framework.permissions import BasePermission

class IsStaff(BasePermission):
    """
    Allows access only to admin users (is_staff=True).
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
    
    
    
class IsStaffOrOwner(BasePermission):
    """
    Custom permission to only allow staff or the owner of the student profile
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user