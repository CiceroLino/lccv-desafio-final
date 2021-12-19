from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.NaturezaDespeza)
admin.site.register(models.Projetos)
admin.site.register(models.Fornecedores)
admin.site.register(models.Ordens)
admin.site.register(models.Vigencias)