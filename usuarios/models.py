from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User  

# Tabela Sessão
class Usuario(models.Model):
    user = models.OneToOneField(auth_models.User, on_delete=models.CASCADE, primary_key=True)  # Relacionamento um para um com o modelo User do Django
    data_nascimento = models.DateField(null=True, blank=True)  # Campo opcional para data de nascimento
    telefone = models.CharField(max_length=20, null=True, blank=True)  # Campo opcional para telefone

class Visitante(models.Model):
    id_visitante = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=45)
    # *Senha não é mais armazenada na tabela Visitante*

class Receita(models.Model):
    id_receita = models.AutoField(primary_key=True)
    nome_receita = models.CharField(max_length=100)
    descricao = models.TextField()
    modo_de_preparo = models.TextField()
    url_audioreceita = models.URLField(blank=True, null=True)
    url_imagemreceita = models.URLField(blank=True, null=True)


    def str(self):
        return self.nome_receita

class Ingrediente(models.Model):

    idingredientes = models.AutoField(primary_key=True)
    tipo_ingredientes = models.CharField(max_length=255)
    nome_ingredientes = models.CharField(max_length=255)

# Tabela Livro de Receitas
class LivroReceitas(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    ingredientes = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

# Tabela Pagamento
class Pagamento(models.Model):
    id_pagamento = models.AutoField(primary_key=True)
    forma_pagamento = models.CharField(max_length=255)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    valor_pagamento = models.DecimalField(max_digits=10, decimal_places=2)

# Tabela Usuários Premium
class UsuariosPremium(models.Model):
    usuario = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(null=True,blank=True)