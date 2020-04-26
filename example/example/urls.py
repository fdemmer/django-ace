from django.contrib import admin
from django.urls import path

from .app.views import simple

urlpatterns = [
    path('admin', admin.site.urls),
    path('', simple),
]
