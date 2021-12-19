from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Model NaturezaDespeza
class NaturezaDespeza(models.Model):
    id_natureza_despeza = models.AutoField(primary_key=True)
    cod_natureza_despeza = models.CharField(max_length=8)
    desc_natureza_despeza = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return self.desc_natureza_despeza
    
# Model Projetos

class Projetos(models.Model):
    id_projeto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    dt_inicio_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField()
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_alt', null=True)
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)
    
    def __str__(self) -> str:
        return self.titulo

# Model Fornecedores

class Fornecedores(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=20)
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_alt', null=True)
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)
    
    def __str__(self) -> str:
        return self.razao_social

# Model Ordens

class Ordens(models.Model):
    id_ordem = models.AutoField(primary_key=True)
    id_projeto = models.IntegerField()
    
    def __str__(self) -> str:
        return self.id_ordem

# Model Vigencias

class Vigencias(models.Model):
    id_vigencia = models.AutoField(primary_key=True)
    id_contrato = models.IntegerField()
    dt_inicio_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=  2)
   
    def __str__(self) -> str:
        return self.id_vigencia
    
# Model Contratos
