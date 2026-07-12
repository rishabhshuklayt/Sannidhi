from django.urls import path 
from .views import RegisterView , LoginView, ProfileUpdateView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name="login"),
    # path("logout/", LoginView.as_view(), name="logout")
    # path("reset-password/", LoginView.as_view(), name="reset-password")
    # path("change-password/", LoginView.as_view(), name="change-password")
    # path("verify-email/", LoginView.as_view(), name="verify-email")
    # path("resend-verification-email/", LoginView.as_view(), name="resend-verification-email")
    # path("refresh-token/", LoginView.as_view(), name="refresh-token")
    # path("revoke-token/", LoginView.as_view(), name="revoke-token")
    # path("get-user-profile/", LoginView.as_view(), name="get-user-profile")
    path("update-user-profile/", ProfileUpdateView.as_view(), name="update-user-profile")
    # path("delete-user-account/", LoginView.as_view(), name="delete-user-account")
    # path("list-users/", LoginView.as_view(), name="list-users")
    # path("get-user-by-id/<int:user_id>/", LoginView.as_view(), name="get-user-by-id")
    # path("get-user-by-email/<str:email>/", LoginView.as_view(), name="get-user-by-email")
    # path("get-user-by-username/<str:username>/", LoginView.as_view(), name="get-user-by-username")
]