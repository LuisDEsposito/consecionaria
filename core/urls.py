from django.urls import path
from django.contrib.auth.views import LogoutView
from core.views import index, CustomLoginView, register, about_me
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name = "core/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("about/me/", about_me, name="about_me"),
    ]

urlpatterns += staticfiles_urlpatterns()