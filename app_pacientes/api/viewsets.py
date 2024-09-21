from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from app_pacientes.models import Pacientes
from app_pacientes.api.serializers import PacienteSerializer, PacienteDetalhesSerializer

class PacientesViewSet(ModelViewSet):
    
    serializer_class = PacienteSerializer
    queryset = Pacientes.objects.all()

    @action(detail=True, methods=["get"])
    def detalhes(self, request, pk=None, *args, **kwargs):
        self.serializer_class = PacienteDetalhesSerializer
        queryset = Pacientes.objects.filter(pk=pk)
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data)