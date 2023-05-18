from django.urls import path
from .views import SignUpView, LoginView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
