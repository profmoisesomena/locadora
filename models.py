# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Categoria(models.Model):
    cod_categoria = models.IntegerField(primary_key=True)
    dsc_categoria = models.CharField(max_length=45)
    vl_categoria = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'categoria'


class Cliente(models.Model):
    cod_cliente = models.IntegerField(primary_key=True)
    nome_cliente = models.CharField(max_length=45, blank=True, null=True)
    dat_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Filme(models.Model):
    cod_filme = models.IntegerField(primary_key=True)
    nome_filme = models.CharField(max_length=50)
    dt_compra = models.DateField(blank=True, null=True)
    vl_filme = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ind_pais = models.IntegerField(blank=True, null=True)
    cod_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='cod_categoria')

    class Meta:
        managed = False
        db_table = 'filme'


class Locacao(models.Model):
    cod_locacao = models.IntegerField(primary_key=True)
    dat_inilocacao = models.DateField()
    dat_fimlocacao = models.DateField(blank=True, null=True)
    vl_multa = models.FloatField(blank=True, null=True)
    cod_filme = models.ForeignKey(Filme, models.DO_NOTHING, db_column='cod_filme')
    cod_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cod_cliente')

    class Meta:
        managed = False
        db_table = 'locacao'
