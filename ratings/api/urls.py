from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'films', views.FilmViewSet, basename="film")
router.register(r'ratings', views.RatingsViewSet , basename="rating")
router.register(r'actors', views.ActorViewSet, basename="actor")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
