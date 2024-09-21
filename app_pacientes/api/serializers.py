from rest_framework.serializers import ModelSerializer
from app_pacientes.models import Pacientes
from app_agendamentos.api.serializers import AgendamentosSerializer

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Pacientes
        fields = "__all__"

class PacienteDetalhesSerializer(ModelSerializer):
    agendamentos = AgendamentosSerializer(many=True, read_only=True) 
    class Meta:
        model = Pacientes
        fields = [
                "id_paciente",
                "nome",
                "rg",
                "data_nascimento",
                "endereco",
                "endereco_numero",
                "endereco_bairro",
                "endereco_cep",
                "data_registro_bd",
                "agendamentos"
        ]