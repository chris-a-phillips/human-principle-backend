from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrincipleViewSet, GoalViewSet

# create the router and register books and authors routes
router = DefaultRouter()
router.register(r'principles', PrincipleViewSet, basename='principle')
router.register(r'goals', GoalViewSet, basename='goal')
urlpatterns = router.urls
