import urllib.parse

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.twitch.provider import TwitchProvider
from allauth.socialaccount.providers.twitch.views import TwitchOAuth2Adapter

from django.http import JsonResponse, response
from django.urls import reverse
from django.shortcuts import redirect


from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView, SocialConnectView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from dj_rest_auth.registration.serializers import (
#     SocialAccountSerializer, SocialConnectSerializer, SocialLoginSerializer,
#     VerifyEmailSerializer, ResendEmailVerificationSerializer
# )

# class TwitchConnect(SocialLoginView):
#     client_class = OAuth2Client
#     # adapter_class = TwitchOAuth2Adapter
#     adapter_class = FacebookOAuth2Adapter 

#     @property
#     def callback_url(self):
#         return self.request.build_absolute_uri(reverse('google_callback'))


# def facebook_callback(request):
#     url = 'http://localhost:3000'
#     params = urllib.parse.urlencode(request.GET)
#     print(params)
#     return redirect(f'{url}/twitch/{params}')
    # using jsonresponse as a placeholder until frontend params are finished
    # return JsonResponse(params, safe=False)


class GoogleConnect(SocialLoginView):
    client_class = OAuth2Client
    # adapter_class = TwitchOAuth2Adapter
    adapter_class = GoogleOAuth2Adapter 

    @property
    def callback_url(self):
        return self.request.build_absolute_uri(reverse('google_callback'))


def google_callback(request):
    url = 'http://localhost:3000'
    params = urllib.parse.urlencode(request.GET)
    print(params)
    return redirect(f'{url}/twitch/{params}')
    # using jsonresponse as a placeholder until frontend params are finished
    # return JsonResponse(params, safe=False)
