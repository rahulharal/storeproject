"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from  crud import views as crud_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add_branch$', crud_view.add_branch),
    url(r'^add_brand$', crud_view.add_brand),
    url(r'^add_product$', crud_view.add_product),
    url(r'^add_store$', crud_view.add_store),
    url(r'^show_store$', crud_view.show_store),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+\
   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)