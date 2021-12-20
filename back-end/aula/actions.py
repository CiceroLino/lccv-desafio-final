from django.utils.translation import ngettext
from django.contrib import messages

def atualiza_fornecedores(modaladmin, request, fornecedores):
    
    for fornecedor in fornecedores:
        fornecedor.razao_social = "teste action"
        fornecedor.save()
        
    modaladmin.message_user(request, ngettext(
        'Fornecedor foi atualizado.',
        'Fornecedores foram atualizados.',
        len(fornecedores)
    ))