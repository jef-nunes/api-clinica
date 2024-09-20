from rest_framework.viewsets import ModelViewSet
from app_agendamentos.models import Agendamentos
from app_agendamentos.api.serializers import AgendamentosSerializer

class AgendamentoViewSet(ModelViewSet):
    serializer_class = AgendamentosSerializer
    queryset = Agendamentos.objects.all().order_by("datahora_agendado")