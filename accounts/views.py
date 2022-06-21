from rest_framework import viewsets
from rest_framework import permissions

from accounts.models import Person
from accounts.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed.
    """
    serializer_class = PersonSerializer
    queryset = Person.objects.order_by('-created_date')
