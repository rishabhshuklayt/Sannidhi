from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)

    username = serializers.CharField(
        required=True,
        max_length=150
    )

    password = serializers.CharField(
        required=True,
        min_length=8
    )

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)

    password = serializers.CharField(
        required=True,
        min_length=8
    )    