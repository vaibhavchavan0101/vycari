from django.views.decorators.cache import never_cache
from social_core.actions import do_auth, do_complete
from social_django.views import _do_login
from django.views.decorators.csrf import csrf_exempt
from social_django.utils import psa, maybe_require_post
from rest_framework.decorators import api_view
from social_django.utils import load_strategy
from social_django.strategy import DjangoStrategy
from social_core.backends.google import GoogleOAuth2, BaseGoogleAuth, BaseGoogleOAuth2API
from social_core.backends.twitter import TwitterOAuth
from drf_social_oauth2.authentication import SocialAuthentication
from social_core.pipeline import user, social_auth       
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth import REDIRECT_FIELD_NAME
import requests
import json
NAMESPACE = "social"

# @api_view(['GET'])
@never_cache
@maybe_require_post
@psa(f"{NAMESPACE}:complete")
def auth(request, backend):
    print('backend 1:--->', backend)
    ss= do_auth(request.backend, redirect_name=REDIRECT_FIELD_NAME)
    print('ss:--->', ss)
    return ss

@never_cache
@csrf_exempt   
@psa(f"{NAMESPACE}:complete")
def get_token(request, backend, *args, **kwargs):
    """Authentication complete view"""
    print('access_token=====:--->', request)
    print('access_token=====:--->', request.backend)
    ss= do_complete(
        request.backend,
        _do_login,
        user=request.user,
        redirect_name=REDIRECT_FIELD_NAME,
        request=request,
        *args,
        **kwargs,
    )
    print('sss:--->', ss)
    return ss
    
def dashboard(request, backend):
    return HttpRequest("Welcome to the dashboard")
