from rest_framework import serializers


from api.models import Computer


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
