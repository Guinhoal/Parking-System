from django.db import models
from django.utils import timezone
from datetime import timedelta
import math

# Create your models here.
class Car(models.Model):
    placa = models.CharField(max_length=10, verbose_name="Placa")
    entrada = models.DateTimeField(auto_now_add=True, verbose_name="Horário de Entrada")
    saida = models.DateTimeField(null=True, blank=True, verbose_name="Horário de Saída")
    pago = models.BooleanField(default=False, verbose_name="Pagamento Realizado")
    
    def __str__(self):
        return f"Carro {self.placa} - {'Estacionado' if not self.saida else 'Saiu'}"
    
    