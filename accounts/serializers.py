from rest_framework import serializers

from accounts.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="accounts:persons-detail")
    class Meta:
        model = Person
        exclude = ('phone', )
        read_only_fields = ('first_name', 'last_name', 'email', 'created_date')
