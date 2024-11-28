from Classes import *
from Funcoes import *
from listas import *
from ObjetosPessoas import *

choice = 10

while choice != 0:
    print("=" * 3, "OPCOES DO CLIENTE", "=" * 9, )
    #acha_nome_por_id(int(input("Digite seu ID : "))) #criar verificacao
    id_atual  = int(input("Digite seu ID :"))

    print(f"Bem vindo novamente {acha_nome_por_id(id_atual,clientes)}! \n[1] Consultar minha reserva \n[2] Alterar minha reserva \n[3]Fazer consumo no Hotel ")
    choice = int(input("Resposta : "))
    print("=" * 31)

    if choice == 1:
        acha_reserva_por_id(id_atual,reservas,quartos)

    if choice == 2:
        pass
    else :
        break