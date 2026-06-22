from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers.user_serializer import RegisterSerializer
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
            })

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
            
        }) 