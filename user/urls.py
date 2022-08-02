from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserViewSet

router = SimpleRouter()
router.register('user', UserViewSet, basename='user')  # /user/
urlpatterns = [
    path('', include(router.urls))
]