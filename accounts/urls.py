from django.urls import path, include
from rest_framework import routers

from accounts.views import PersonViewSet

app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet, basename='persons')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
