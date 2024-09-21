from rest_framework.viewsets import ModelViewSet
from app_historicos.models import Historicos
from app_historicos.api.serializers import HistoricosSerializer

class HistoricosViewSet(ModelViewSet):
    serializer_class = HistoricosSerializer
    queryset = Historicos.objects.all().order_by("data_registro_bd")