from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, PrincipleViewSet

# create the router and register books and authors routes
router = DefaultRouter()
router.register(r'members', MemberViewSet, basename='member')
router.register(r'principles', PrincipleViewSet, basename='principle')
urlpatterns = router.urls
