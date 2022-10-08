from rest_framework import serializers
from .models import Project, Measurement


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class MeasurmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"
