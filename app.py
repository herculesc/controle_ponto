"""
Controle de horas, um ponto eletrônico que calcula
a quantidade de horas trabalhadas.

É necessario armazenar a data -> calcular a

hora de entrada - hora de saida do trabalho

"""
# Criar marcacao de ponto
# Dicionario data: valor, hora_entrada: valor, horad_saida
# Calcular horas trabalhadas



# Salvar ponto
import datetime

# Retorna data e hora
def data_time():
    data_time_now = datetime.datetime.now()
    return data_time_now

def data():
    data_time_now = data_time()
    data_now = data_time_now.date()
    return data_now

def horario():
    data_time_inicial = data_time()
    time = data_time_inicial.time()
    return time

# Manter essa variavel ?
def exit_time():
    exit_time_now = input('saida: ')
    return exit_time_now


def criar_cartao_ponto(dicionario, data, hora_entrada, hora_saida):
    dicionario = ['Data':data,'Hora-Entrada':hora_entrada,'Hora-saida': hora_saida]



data_time = datetime.datetime.now()

# Data
data = data_time.date()

# horario de entrada
time = data_time.time()
print(f"data: {day} time: {time}")





