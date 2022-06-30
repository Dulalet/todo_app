from django.urls import path, include
from .views import AuthViewSet


urlpatterns = [
    path('login/', AuthViewSet.as_view({'post': 'login'}), name='login'),
    path('register/', AuthViewSet.as_view({'post': 'register'}), name='register'),
    path('logout/', AuthViewSet.as_view({'post': 'logout'}), name='logout'),
    path('getUser/', AuthViewSet.as_view({'get': 'get_user'}), name='getuser'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
