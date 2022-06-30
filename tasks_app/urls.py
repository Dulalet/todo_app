from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'todo', TaskViewSet, basename='todo')


urlpatterns = [
    path('api/', include(router.urls))
]

