"""template_new URL Configuration

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
"""
from django.conf.urls import url,include
from django.contrib import admin

''' 
urlpatterns define set of valid urls which can be used as web pages.

The first pattern says localhost/admin/ is a valid url. This is the link for admin page where we can manage our minutes details

The second pattern lines to minutes.urls function. It deals with other urls. For furthur details visit minutes.urls

'''

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('minutes.urls'))
]
