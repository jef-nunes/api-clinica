from django.db.models import Model, AutoField, CharField, \
    DateTimeField, IntegerField

# entidade paciente
class Pacientes(Model):
    id_paciente = AutoField(primary_key=True)
    nome = CharField(max_length=100, blank=True, null=True)
    rg = CharField(max_length=100, blank=True, null=True)
    data_nascimento = DateTimeField(blank=True,null=True)
    endereco = CharField(max_length=100)
    endereco_numero = IntegerField(blank=True, null=True)
    endereco_bairro = CharField(max_length=100, blank=True, null=True)
    endereco_cep = CharField(max_length=100, blank=True, null=True)
    data_cadastro = DateTimeField(auto_now_add=True)

    class Meta:
        # ativar o gerenciamento do
        #  banco de dados pelo django
        managed = True
        # nome da tabela
        db_table = 'pacientes'

    def __str__(self):
        return f"{self.nome} ({self.rg})"