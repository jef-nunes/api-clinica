from rest_framework.serializers import ModelSerializer
from app_pacientes.models import Pacientes

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Pacientes
        fields = "__all__"