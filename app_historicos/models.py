from django.db.models import Model, AutoField, DateTimeField, \
    BooleanField, TextField, CharField, ForeignKey, CASCADE
from app_agendamentos.models import Agendamentos

class Historicos(Model):
    id_historico = AutoField(primary_key=True)
    data_registro_bd = DateTimeField(auto_now_add=True)
    sintomas_surgimento = CharField(max_length=100, blank=True, null=True)
    sintomas_duracao = CharField(max_length=100,blank=True,null=True)
    dor_localizar = CharField(max_length=100, blank=True, null=True)
    dor_tipo = CharField(max_length=100, blank=True, null=True)
    conclusao = TextField(blank=True, null=True)
    id_agendamento = ForeignKey(Agendamentos,related_name="historicos",
                                 on_delete=CASCADE, blank=False, null=False)
    
    class Meta:
        managed = True
        db_table = 'historicos'