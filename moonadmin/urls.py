from django.urls import path
from .views import LoginAdminView

urlpatterns = [
    path("login/", LoginAdminView.as_view()),
]
