from django.db.models import Model, AutoField, DateTimeField, \
    BooleanField, TextField, CharField, ForeignKey, CASCADE

from app_pacientes.models import Pacientes

class Agendamentos(Model):
    id_agendamento = AutoField(primary_key=True)
    categoria = CharField(max_length=100, blank=True, null=True)
    observacoes = TextField(blank=True, null=True)
    datahora_agendado = DateTimeField(blank=False, null=False)
    cancelado = BooleanField(default=False)
    data_registro_bd = DateTimeField(auto_now_add=True)
    # relacionamento
    id_paciente = ForeignKey(Pacientes, on_delete=CASCADE,
                             related_name='agendamentos', blank=False, null = False)

    class Meta:
        managed = True
        db_table = 'agendamentos'
        unique_together = ('datahora_agendado', 'id_paciente')