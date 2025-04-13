# Sistema de Estacionamento (Parking System)
Sistema web para gerenciamento de estacionamentos desenvolvido com Django.

## Descrição
Este sistema permite o gerenciamento completo de um estacionamento, incluindo:

- Registro de entrada e saída de veículos
- Cálculo automático de valores a serem pagos
- Controle de pagamentos
- Dashboard com estatísticas gerais


## Pré-requisitos
- Python (3.8 ou superior)
- Django (4.0 ou superior)
- [Git](https://git-scm.com/downloads) (Opcional) para facilitar o uso do GitHub
- Editor de texto, [Visual Studio Code](https://code.visualstudio.com/)
  
## Estrutura do Projeto
- `parking_system` - Pasta principal do projeto Django
- `parking_systems`/ - Aplicação principal
- `models.py` - Definição do modelo de dados
- `views.py` - Lógica de controle
- `urls.py` - Rotas da aplicação
- `templates/parking_systems/` - Templates HTML
- `static/parking_systems/` - Arquivos estáticos (CSS e imagens)

## Instalação
Para instalar o sistema e utiliza-lo no computador usando git, você pode usar os seguintes comandos:

Clona o repositorio na sua maquina:

```bash
git clone https://github.com/seu-usuario/Parking-System.git
cd Parking-System
```

Crie um ambiente virtual (opcional):

```bash
python -m venv venv
```

Ative o ambiente virtual (No windows):

```bash
venv\Scripts\activate
```

No macOS e Linux:

```bash
source venv/bin/activate
```

Execute as migrações:

```bash
cd parking_system
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse o sistema em http://127.0.0.1:8000/


## Funcionalidades
### Entrada de Veículos
- Registra a placa do veículo
- Armazena automaticamente data e hora de entrada
### Saída de Veículos
- Registra a saída do veículo através da placa
- Calcula automaticamente o tempo de permanência
- Gera valor a ser pago com base na tabela de preços
### Pagamento
- Interface para confirmação de pagamento
- Registro de status de pagamento
### Dashboard
- Visualização de veículos atualmente estacionados
- Estatísticas gerais (total de entradas, saídas, valores)
### Regras de Negócio
Cálculo de Valor
- Primeira hora: R$ 5,00
- Horas adicionais: R$ 2,00 por hora
- O tempo é arredondado para cima (ex: 1h30min = 2h)

## Admin Django
Caso queira acessar o painel de administrador do Django para conferir o modelo de Carro, faça 

Criar superusuário (admin):

```bash
python manage.py runserver
```

Acessar o painel de administração: http://127.0.0.1:8000/admin/

## Sobre a Solução:
    	Em uma síntese rápida de como foi feito o projeto, inicialmente foi criado o repositório no GitHub e clonado para dentro do Vs Code, neste através da linha de comando foi criado um ambiente virtual em python e iniciado o servidor Django, após iniciado o servidor, foi criado o App, seguindo a norma do plural (Nome do Projeto + s = Nome do App).
        Após a criação do APP já realizei a troca dos endpoints em urls do projeto para redirecionar para as urls do app em todos os casos fora para o endpoint de admin (Página de administração do Django)
        Dentro dos models do app criei somente um para facilitar o projeto, determinei campos essenciais e métodos para cálculo, usei o DB Browser para a verificação
        Criei então os templates para ajudar na visualização do que deve ser feito, além disso coloquei no caminho static o css e a favicon usadas, após isso para o término simples da explicação, configurei as views com as funções para obtenção de dados e os render necessários, Por fim alterei os templates para exibir as "variaveis" antes configuradas nos métodos views
## Detalhes Importantes:
### Uso da IA:
- Usada para ajudar na estilização das páginas html
### Considerações:
- É possível devido a falta de conhecimento que o nome de alguma variavel ou método não esteja de acordo com os padrões utilizados
- O dashboard não possui algumas informações, como os relatórios do dia ou da semana, já que não consegui realizar essas marcas temporais
- O horário esta 3 horas a frente do de Brasília, algo que também não encontrei solução simples



## Contribuidor
[Thiago Arthur](https://github.com/Guinhoal)
