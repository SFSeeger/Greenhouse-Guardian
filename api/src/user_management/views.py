from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication


class LoginView(KnoxLoginView):
    throttle_scope = "login"
    authentication_classes = [BasicAuthentication]