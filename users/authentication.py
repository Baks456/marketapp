from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            return None

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(pk=user_id)
            return user
        except user_model.DoesNotExist:
            return None
