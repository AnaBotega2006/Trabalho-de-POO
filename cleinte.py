from Classes import *
from Funcoes import *
from listas import *
from ObjetosPessoas import *

choice = 1


while choice != 0:

    #acha_nome_por_id(int(input("Digite seu ID : "))) #criar verificacao
    id_atual  = int(input("Digite seu ID :"))
    vip = acha_vip_por_id(id_atual,clientes)
    print(vip)

    """print(f"Bem vindo novamente{acha_nome_por_id(id_atual,clientes)}!\n[1]Alugar Quarto \n[2] Consultar minha reserva \n[3] Alterar minha reserva(exclusivo VIP) \n[3]Fazer consumo no Hotel\n[0]Sair ")
    choice = int(input("Resposta : "))
    print("=" * 31) """

    if choice == 1:
        """"quantd_desejada = int(input("Quantidade de pessoas : "))
        data_checkin = int(input("Dia do check-in : "))
        data_checkout = int(input("Data do check-out : "))"""
        a = gera_quartos_disponiveis(reservas,quartos)
        b = gera_quartos_disponiveis_jaalugados(reservas,quartos,dias)
        print(b)
        gera_quartos_disponiveis_pordata(1,1,0,a,b)

    if choice == 2:
        acha_reserva_por_id(id_atual,reservas,quartos)

    if choice == 3 and vip == 1:
        print("=" * 3, "MENU DE ALTERACAO", "=" * 9, )
        print("O que gostaria de alterar? : ")
        mudar = int(input(("[1]Mudar de Quarto \n[2]Mudar data de Check-In \n[3]Mudar data de Check-Out\n[0]Sair\nResposta : ")))
        print("=" * 31)

        if mudar == 1:
            print("=" * 3, "MENU DE ALTERACAO", "=" * 9, )
            print("Quartos disponiveis para a mesma quantidade de pessoas : ")
            print("OBS : Os quartos a seguir possuem disponibilidade de acordo com\nseu dia de check-in e check-out")

    elif choice == 0 :
        break


        #AQUII


            #selecionar quarto
            #tirar esse da lista de ocupados e botar na livre
            #tirar o escolhido dos livres e colocar nos ocupados

    else :
        break




