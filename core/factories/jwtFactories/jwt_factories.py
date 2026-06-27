from core.adapters.JwtAdapters.simple_jwt_adapter import Simple_JWT_Adapter\

class JWTFactories:
    @staticmethod
    def get_jwt_adapter():
        return Simple_JWT_Adapter()