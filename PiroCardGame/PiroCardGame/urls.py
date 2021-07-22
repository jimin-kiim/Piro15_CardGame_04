
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name="users/login.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
]
