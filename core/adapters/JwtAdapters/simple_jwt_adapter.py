from core.ports.jwt_port.jwt_port import JWTPort

class Simple_JWT_Adapter(JWTPort):
   def generate_token(self, user_id: int) -> str:
      pass
   