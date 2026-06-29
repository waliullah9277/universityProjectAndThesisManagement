from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "STUDENT"


class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "SUPERVISOR"


class IsExaminer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "EXAMINER"


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "ADMIN"