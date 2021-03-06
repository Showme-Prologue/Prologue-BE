"""config URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

#from introduction.views import IntroductionListViewSet, IntroductionComponentListViewSet, IntroductionQuestionListViewSet
from introduction import views
import introduction.urls, account.urls, group.urls

# router = routers.DefaultRouter()
# router.register('introduction', IntroductionListViewSet)
# router.register('introductionComponent', IntroductionComponentListViewSet)
# router.register('introductionQuestion', IntroductionQuestionListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include(router.urls)),
    path('api/', include(introduction.urls)),
    path('api/', include(account.urls)),
    path('api/', include(group.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)