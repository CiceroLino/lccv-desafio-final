from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from . import models

@receiver(pre_save, sender=models.Fornecedores)

def teste_pre_save(sender, instance, **kwargs):
    print("================ pre_save ====================")
    
    instance.razao_social = 'Pre Save'
    
@receiver(post_save, sender=models.Fornecedores)
def test_post_save(sender, instance, **kwargs):
    print("================ post_save ====================")
    
    instance.razao_social = 'Post Save'
    #instance.save()
    
