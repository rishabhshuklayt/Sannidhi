from core.ports.jwt_port.jwt_port import JWTPort
from rest_framework_simplejwt.tokens import RefreshToken

class Simple_JWT_Adapter(JWTPort):
   def generate_token(self, user_id):
      refresh_token = RefreshToken.for_user(user_id)
      access_token = refresh_token.access_token
      return {
         "refresh_token": str(refresh_token),
         "access_token": str(access_token)
      }