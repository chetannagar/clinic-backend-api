from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serializers import (
    UserSerializer,
    RegisterPatientSerializer,
    RegisterDoctorSerializer,
    LoginSerializer,
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterPatientView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterPatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class RegisterDoctorView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterDoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, email=serializer.validated_data["email"])
        if not user.check_password(serializer.validated_data["password"]):
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteUserView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({"detail": "user_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
