from django.contrib import admin
from django.urls import path, include
from . import views
from .views import health_check

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path("sentry-key-error/", views.trigger_key_error),
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health_check'),
    ]

handler404 = "oc_lettings_site.views.warning_404"
handler500 = "oc_lettings_site.views.error_500"
