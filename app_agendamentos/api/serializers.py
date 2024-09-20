from rest_framework.serializers import ModelSerializer
from app_agendamentos.models import Agendamentos

class AgendamentosSerializer(ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = "__all__"