"""JackTracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

    add package urls in this one
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
import debug_toolbar

urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^jack/', include('jack.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^rental/', include('rental.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    #url(r'^account/login/$', 'django.contrib.auth.views.login',{('template_name'): ('registration/login.html')}),
    #url(r'^account/logout/$', 'django.contrib.auth.views.logout',{('template_name'): ('registration/logout.html')}),
    url(r'^__debug__/', include(debug_toolbar.urls)),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns