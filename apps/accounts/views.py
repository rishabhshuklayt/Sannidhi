from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers.user_serializer import LoginSerializer, RegisterSerializer
from .services.auth_services import AuthService
from .repository.user_repository import UserRepository
from core.factories.email_factories import EmailFactory
class RegisterView(APIView):

    def post(self, request):

        if not request.method == "POST":
            return Response({
                "message": "Invalid request method"
            })

        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                "message": "Invalid data provided"
            }, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        username = serializer.validated_data.get("username")

        service = AuthService(
            user_repository = UserRepository,
            email_port = EmailFactory
        )

        user = service.register_user(username=username, email=email, password=password)

        if not user:
            return Response({
                "message": "User registration failed"
            })
        
        print(f"User registered with email: {user}")

        return Response({
            "email": user.email,
            "message": "User registered", 
        }, status=status.HTTP_201_CREATED) 
    



class LoginView(APIView):

    def post(self, request):
        if not request.method == "POST":
            return Response({
                "message": "Invalid request method"
            })
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "message": "Invalid data provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        service = AuthService(
            user_repository = UserRepository,
            email_port = EmailFactory
        )
        
        user = service.login_user(email=email, password=password)

        if not user:
            return Response({
                "message": "Login failed"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "message": "Login successful"
        }, status=status.HTTP_200_OK)    