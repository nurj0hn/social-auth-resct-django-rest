import debug_toolbar

from django.contrib import admin
from django.urls import path, include
from .views import  google_callback, GoogleConnect
from allauth.socialaccount.providers.google import views as twitch_views


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('nimda/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('twitch/connect/', GoogleConnect.as_view(), name='twitch_connect'),
    path('auth/login/', twitch_views.oauth2_login, name='facebook_login'),
    path('auth/login/callback/', google_callback, name='google_callback'),
    # path('accounts/', include('allauth.urls')),
    path('tasks/', include('tasks.urls')),
    path('users/', include('users.urls')),
]