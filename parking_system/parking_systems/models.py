from django.db import models
from django.utils import timezone
from datetime import timedelta
import math

class Car(models.Model):
    """"Campos do Banco de dados"""
    placa = models.CharField(max_length=10, verbose_name="Placa")
    entrada = models.DateTimeField(auto_now_add=True, verbose_name="Horário de Entrada")
    saida = models.DateTimeField(null=True, blank=True, verbose_name="Horário de Saída")
    pago = models.BooleanField(default=False, verbose_name="Pagamento Realizado")
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Valor a Pagar")
    

    def __str__(self):
        return f"Carro {self.placa} - {'Estacionado' if not self.saida else 'Saiu'}"
    

    """"Cálculo"""
    def calcular_valor(self):
        if not self.saida:
            return None
        
        duracao = self.saida - self.entrada
        minutos_totais = duracao.total_seconds() / 60
        
        horas = math.ceil(minutos_totais / 60)
        
        if horas <= 1:
            return 5.00  
        else:
            return 5.00 + (horas - 1) * 2.00 
    
    def tempo_permanencia(self):
        if not self.saida:
            duracao = timezone.now() - self.entrada
        else:
            duracao = self.saida - self.entrada
        
        horas = duracao.seconds // 3600
        minutos = (duracao.seconds % 3600) // 60
        
        if duracao.days > 0:
            return f"{duracao.days} dias, {horas}h e {minutos}min"
        else:
            return f"{horas}h e {minutos}min"
            
    def status_pagamento(self):
        if not self.saida:
            return "Estacionado"
        elif self.pago:
            return "Pago"
        else:
            return "Pendente"