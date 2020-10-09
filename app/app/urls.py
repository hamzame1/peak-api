"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from peak import views
from django.conf.urls.static import static

from app import settings
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('user.urls')),
    path('api/getpeak', views.get_Peak,name="get_peak"),
    path('api/addpeak/', views.add_Peak,name="add_peak"),
    path('api/updatepeak/<int:peak_id>',views.update_peak,name="update_peak"),
    path('deletepeak/<int:peak_id>', views.delete_peak,name="delete_peak"),
    path('', TemplateView.as_view(template_name="index.html"),name="index"),
    path('documentation/', TemplateView.as_view(template_name="documentation.html"),name="documentation")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
