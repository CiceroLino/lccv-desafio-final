from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Model NaturezaDespesa
class NaturezaDespesa(models.Model):
    id_natureza_despesa = models.AutoField(primary_key=True)
    cod_natureza_despesa = models.CharField(max_length=8)
    desc_natureza_despesa = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return self.desc_natureza_despesa
    
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
    id_projeto = models.ForeignKey(Projetos, on_delete=models.Case)
    id_fornecedor = models.ForeignKey(Fornecedores, on_delete=models.Case)
    id_natureza_despesa = models.ForeignKey(NaturezaDespesa, on_delete=models.Case)
    numero = models.IntegerField()
    ano = models.IntegerField()
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_alt', null=True)
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)
        
    def __str__(self) -> str:
        return str(self.id_projeto) + '/' + str(self.id_fornecedor)

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

class Contratos(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    id_prestador = models.ForeignKey(Fornecedores, on_delete=models.Case)
    numero = models.IntegerField()
    ano = models.IntegerField()
    data_inicio_vigencia = models.DateField()
    data_fim_vigencia = models.DateField()
    objeto = models.CharField(max_length=25)
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_alt', null=True)
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id_prestador) + '/' + str(self.id_contrato)

# Model Itens Contratos

class ItensContrato(models.Model):
    id_item_contrato = models.AutoField(primary_key=True)
    id_contrato = models.IntegerField()
    id_item_ordem = models.IntegerField()
    qtd = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=  2)
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_alt', null=True)
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id_item_contrato) + '/' + str(self.id_item_ordem)

# Model Itens Ordens

class ItensOrdem(models.Model):
    id_item_ordem = models.AutoField(primary_key=True)
    id_ordem = models.IntegerField()
    produto_servico = models.CharField(max_length=100)
    qtd = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=  2)
    id_user_cad = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user_alt', null=True)
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id_item_ordem) + '/' + str(self.id_ordem)