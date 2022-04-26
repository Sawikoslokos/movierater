from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api import urls


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls))
]
