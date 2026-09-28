"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
# This imports Django's built-in admin functionality. It allows: /admin/  to access the Django admin panel.

from django.urls import path,include
# Used to include URLs from another URL configuration. Ex:-path("api/", include("api.urls"))

from api.views import CreateUserView
# "Go into the api application's views.py and bring me CreateUserView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# There are two important operations here.

# Token obtain
# TokenObtainPairView

# The user sends:

# username
# password

# and Django returns tokens.

# Typically:

# {
#     "access": "...",
#     "refresh": "..."
# }

# TokenRefreshView:When the access token expires, the refresh token can be used to obtain a new access token.

# Conceptually:

# LOGIN
#  ↓
# username + password
#  ↓
# access token + refresh token
#  ↓
# React stores tokens
#  ↓
# API requests use access token
# added above two lines for import

urlpatterns = [
    path('admin/', admin.site.urls),
    # Django sends the request to its admin site.

    # all below four lines added
                      
    path("api/user/register",CreateUserView.as_view(),name="register"),
#     Why .as_view()? CreateUserView is a class. Django's URL system needs a callable view.
# .as_view() converts the class-based view into something Django can call when the URL is requested.

    path("api/token/",TokenObtainPairView.as_view(),name="get_token"),
    # no need manually write login logic as Simple JWT already provides it in TokenObtainPaiviewr.

    path("api/token/refresh/",TokenRefreshView.as_view(),name="refresh"),

    path("api-auth/",include("rest_framework.urls")),
#     This includes DRF's built-in authentication URLs.
# It's commonly used with the Django REST Framework browsable API, 
# particularly for login/logout in the browsable interface.It's different from your JWT authentication.

# So don't think: api-auth = JWT....It isn't.
# You essentially have:
# /api/token/             → JWT login
# /api/token/refresh/     → JWT token refresh
# /api-auth/              → DRF browsable API authentication

    path("api/",include("api.urls")),
]
