from rest_framework import serializers

class UserRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=15)
    last_name = serializers.CharField(max_length=255)
    username = serializers.EmailField()
    password = serializers.CharField()