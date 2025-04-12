from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Car
from django.db.models import Count, Sum, Avg, F, ExpressionWrapper, fields
from django.db.models.functions import TruncDate
from datetime import datetime, timedelta


"""Conta o número de carros estacionados chamada ao entrar no index"""
def index(request):
    veiculos_estacionados = Car.objects.filter(saida__isnull=True).count()
    context = {
        'veiculos_estacionados': veiculos_estacionados
    }
    return render(request, 'parking_systems/index.html', context) 

"""Calcula estastíticas Gerais, chamada ao acessar o dashboard"""
def dashboard(request):
    total_entradas = Car.objects.count()
    veiculos_estacionados = Car.objects.filter(saida__isnull=True).count()
    veiculos_saida = Car.objects.filter(saida__isnull=False).count()
    total_faturado = Car.objects.filter(pago=True).aggregate(total=Sum('valor'))['total'] or 0
    
    
    context = {
        'total_entradas': total_entradas,
        'veiculos_estacionados': veiculos_estacionados,
        'veiculos_saida': veiculos_saida,
        'total_faturado': total_faturado,
    }
    
    return render(request, 'parking_systems/dashboard.html', context)

""""Processa a entrada de veículos e vê se é possível estacionar - Chamada por formulário"""
def car_entry(request):
    if request.method == 'POST':
        placa = request.POST.get('placa').strip().upper()
        if not placa:
            messages.error(request, 'A placa do veículo é obrigatória.')
            return redirect('index')
            
        if Car.objects.filter(placa=placa, saida__isnull=True).exists():
            messages.error(request, f'Veículo com placa {placa} já está no estacionamento!')
        else:
            Car.objects.create(placa=placa)
            messages.success(request, f'Entrada do veículo {placa} registrada com sucesso!')
        
        return redirect('car_list')
        
    return redirect('index')

""""Processa a saída de carro e é chamada por formulário"""
def car_exit(request):
    if request.method == 'POST':
        placa = request.POST.get('placa').strip().upper()
        if not placa:
            messages.error(request, 'A placa do veículo é obrigatória.')
            return redirect('index')
            
        try:
            carro = Car.objects.get(placa=placa, saida__isnull=True)
            
            carro.saida = timezone.now()
            
            carro.valor = carro.calcular_valor()
            
            carro.save()
            
            messages.success(request, f'Saída do veículo {placa} registrada. Valor a pagar: R$ {carro.valor:.2f}')
            return redirect('car_payment', pk=carro.id)
            
        except Car.DoesNotExist:
            messages.error(request, f'Veículo com placa {placa} não encontrado no estacionamento.')
        
        return redirect('car_list')
    
    return redirect('index')


""""Lista todos os veículos"""
def car_list(request):
    carros_estacionados = Car.objects.filter(saida__isnull=True).order_by('-entrada')
    
    context = {
        'carros': carros_estacionados,
        'titulo': 'Veículos Estacionados',
        'total': carros_estacionados.count()
    }
    
    return render(request, 'parking_systems/car_list.html', context)


""""Realiza o pagamento"""
def car_payment(request, pk):
    carro = get_object_or_404(Car, pk=pk)
    
    if request.method == 'POST':
        carro.pago = True
        carro.save()
        messages.success(request, f'Pagamento do veículo {carro.placa} confirmado!')
        return redirect('car_list')
    
    context = {
        'carro': carro,
    }
    
    return render(request, 'parking_systems/car_payment.html', context)

