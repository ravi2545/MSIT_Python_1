from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('kalyan/', include('kalyan.urls')),
    path('admin/', admin.site.urls),
]
