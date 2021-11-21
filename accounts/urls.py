from django.urls import path, include

import dj_rest_auth.urls
import allauth.urls

import accounts.views
import accounts.urls

urlpatterns = [
    path('accounts/', include(dj_rest_auth.urls)),
    path('accounts/', include(allauth.urls)),

    # No Slash
    path('accounts', include(dj_rest_auth.urls)),
    path('accounts', include(allauth.urls)),

    path('accounts/google/login', accounts.views.google_login, name='google_login'),
    path('accounts/google/callback/', accounts.views.google_callback, name='google_callback'),
    path('accounts/google/login/finish/', accounts.views.GoogleLogin.as_view(), name='google_login_todjango'),
]