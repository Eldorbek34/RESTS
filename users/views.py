from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from users.serializers import UserRegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.utils import IntegrityError
User = get_user_model()


class UserRegistrationApiView(GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.POST)
        if serializer.is_valid():
            try:
                user = User.objects.create(
                    first_name=serializer.data.get("first_name"),
                    last_name=serializer.data.get("last_name"),
                    username=serializer.data.get("username"),
                )
                user.set_password(serializer.data.get("password"))
                user.save()

                token = RefreshToken().for_user(user)
                data = {
                    "refresh": str(token),
                    "access": str(token.access_token)
                }
                return Response(data, status=200)
            except IntegrityError:
                raise ValidationError(
                        {"username": "This username is already taken"}
                    )
        return Response(serializer.errors, status=403)