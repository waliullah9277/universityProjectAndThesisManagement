from rest_framework import serializers
from .models import User, UserRole
from .services import UserService
from .models import User, StudentProfile
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    confirm_password = serializers.CharField(
        write_only=True
    )

    class Meta:

        model = User

        fields = (
            "email",
            "first_name",
            "last_name",
            "phone",
            "role",
            "password",
            "confirm_password",
        )

    def validate(self, attrs):

        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "password": "Passwords do not match."
                }
            )

        return attrs

    def create(self, validated_data):

        validated_data.pop("confirm_password")

        return UserService.create_user(validated_data)
    
# Serializer for user profile
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone",
            "role",
            "created_at",
        ]

# Serializer for student profile
class StudentProfileSerializer(serializers.ModelSerializer):
    
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = StudentProfile
        fields = "__all__"


# login serializer
class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):

        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            username=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "User account is inactive."
            )

        attrs["user"] = user

        return attrs

# update profile serializer
class UpdateProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone",
            "role",
        ]



# change password serializer
class ChangePasswordSerializer(serializers.Serializer):

    current_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):

        user = self.context["request"].user

        if not user.check_password(attrs["current_password"]):
            raise serializers.ValidationError({
                "current_password": "Current password is incorrect."
            })

        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({
                "confirm_password": "Passwords do not match."
            })

        validate_password(attrs["new_password"])

        return attrs