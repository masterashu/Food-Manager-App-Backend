from rest_framework import permissions


class IsAuthenticatedOrGet(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.method == 'GET' or super().has_object_permission(request, view, obj)

    def has_permission(self, request, view):
        return request.method == 'GET' or super().has_permission(request, view)
