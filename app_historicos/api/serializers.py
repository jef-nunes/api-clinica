from rest_framework.serializers import ModelSerializer
from app_historicos.models import Historicos

class HistoricosSerializer(ModelSerializer):
    class Meta:
        model = Historicos 
        fields = "__all__"