from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrincipleViewSet

# create the router and register books and authors routes
router = DefaultRouter()
router.register(r'principles', PrincipleViewSet, basename='principle')
urlpatterns = router.urls
