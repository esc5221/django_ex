from django.urls import path, include
from rest_framework.routers import SimpleRouter
from seminar.views import SeminarViewSet

app_name = 'seminar'

router = SimpleRouter()
router.register('seminar', SeminarViewSet, basename='seminar')  # /seminar/
urlpatterns = [
    path('', include(router.urls))
]