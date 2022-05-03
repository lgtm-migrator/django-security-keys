"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

import django_security_keys.views
from two_factor.urls import urlpatterns as tf_urls

from django_security_keys.ext.two_factor.views import LoginView


tf_urls[0][0] = re_path(route=r"^account/login/$", view=LoginView.as_view(), name="login",)

urlpatterns = [
    path('', include(tf_urls)),
    path("admin/", admin.site.urls),
    path("login/", django_security_keys.views.basic_login, name="login"),
    path("logout/", django_security_keys.views.basic_logout, name="logout"),
    path(
        "security-keys/",
        include(
            ("django_security_keys.urls", "django_security_keys"),
            namespace="security-keys",
        ),
    ),
]
