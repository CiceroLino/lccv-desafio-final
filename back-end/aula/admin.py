from django.contrib import admin

from . import models
class FornecedoresForm(admin.ModelAdmin):
    readonly_fields = ['id_user_cad', 'id_user_alt']

admin.site.register(models.NaturezaDespesa)
admin.site.register(models.Projetos)
admin.site.register(models.Fornecedores, FornecedoresForm)
admin.site.register(models.Ordens)
admin.site.register(models.Vigencias)
admin.site.register(models.Contratos)
admin.site.register(models.ItensContrato)
admin.site.register(models.ItensOrdem)