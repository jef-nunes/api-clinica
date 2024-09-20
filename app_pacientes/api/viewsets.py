from rest_framework.viewsets import ModelViewSet
from app_pacientes.models import Pacientes
from app_pacientes.api.serializers import PacienteSerializer

class PacientesViewSet(ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Pacientes.objects.all()