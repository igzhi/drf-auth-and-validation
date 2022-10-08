from rest_framework.viewsets import ModelViewSet
from .models import Project, Measurement
from .serializers import ProjectSerializers, MeasurmentSerializers


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurmentSerializers
