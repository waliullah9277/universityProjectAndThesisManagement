from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import LogoutSerializer, RegisterSerializer, LoginSerializer, UpdateProfileSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ChangePasswordSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStudent

# register API view
class RegisterAPIView(generics.CreateAPIView):

    serializer_class = RegisterSerializer

    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "User registered successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

# APIView for user profile 
class ProfileAPIView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = UserProfileSerializer(request.user)

        return Response({
            "success": True,
            "data": serializer.data
        })

# log in api view
class LoginAPIView(APIView):
    
    permission_classes = []

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "success": True,
                "message": "Login successful.",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role,
                }
            }
        )

# APIView for updating user profile
class UpdateProfileAPIView(APIView):
    
    permission_classes = [IsAuthenticated]

    def put(self, request):

        serializer = UpdateProfileSerializer(
            request.user,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({
            "success": True,
            "message": "Profile updated successfully.",
            "data": serializer.data
        })

# APIView for changing user password
class ChangePasswordAPIView(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = ChangePasswordSerializer(
            data=request.data,
            context={"request": request}
        )

        serializer.is_valid(raise_exception=True)

        request.user.set_password(
            serializer.validated_data["new_password"]
        )

        request.user.save()

        return Response({
            "success": True,
            "message": "Password changed successfully."
        })
    
# logout api view   
class LogoutAPIView(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = LogoutSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({
            "success": True,
            "message": "Logout successful."
        })



# APIView for student only access
class StudentOnlyAPIView(APIView):

    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request):
        return Response({
            "success": True,
            "message": "Welcome Student!",
            "user": request.user.email
        })