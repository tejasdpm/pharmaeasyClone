from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("prescription", views.PrescriptionViewSet)
urlpatterns = [
    path("", views.health, name="health"),
    path("register", views.register, name="register"),
    path("login", views.LoginView.as_view(), name="login"),
    path("test", views.test, name="test")
]

urlpatterns += router.urls
