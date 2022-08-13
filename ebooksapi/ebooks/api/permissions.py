from rest_framework import permissions


class IsAdminUserorReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return bool(request.method in permissions.SAFE_METHODS or is_admin)


class IsReviewAuthororReadOnly(permissions.BasePermission):
    message = "You are not allowed to edit it."
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(obj.review_author == request.user)
