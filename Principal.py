from Classes import *
from ObjetosPessoas import *
from Funcoes import *

# listas de controle
clientes = [c1,c2,c3,c4]
quartos = [q1,q2,q3,q4]
quartos_alugados = []
dias = [1,2,3,4]
disponiveis_dia1 = [q1,q2,q3]
disponiveis_dia2 = [q1,q2,q3]
disponiveis_dia3 = [q1]
disponiveis_dia4 = [q1]
reservas = [["34",0,2],["12",1,1],["14",3,3]]

# variaveis
id_cliente = len(clientes) - 1
codigo = ""
primeira_vez = 0
choice12 = 1000

choice = 1

while choice != 0:
    print("=" * 3, "OPCOES", "=" * 20, )
    print("Já é nosso cliente ? \n[1] Sim \n[2] Nao , quero me casdastrar \n[0] Sair ")
    choice = int(input("Resposta : "))
    choice = check(0, 2, choice)
    primeira_vez = 0
    print("=" * 31)

    if choice == 1:  # Se ja for cliente
        while choice12 != 0:
            if primeira_vez == 0:
                # acha_nome_por_id(int(input("Digite seu ID : "))) #criar verificacao
                id_atual = int(input("Digite seu ID :"))
                vip = acha_vip_por_id(id_atual,clientes)

                print(f"Bem vindo novamente {acha_nome_por_id(id_atual,clientes)}!\n[1]Alugar Quarto \n[2] Consultar minha reserva \n[3] Alterar minha reserva(exclusivo VIP) \n[3]Fazer consumo no Hotel\n[0]Sair ")
                choice12 = int(input("Resposta : "))
                primeira_vez = 1
            else :
                print("=" * 31)
                print( f"[1]Alugar Quarto \n[2] Consultar minha reserva \n[3] Alterar minha reserva(exclusivo VIP) \n[3]Fazer consumo no Hotel\n[0]Sair ")
                choice12 = int(input("Resposta : "))
            print("=" * 31)

            if choice12 == 1: # ALUGAR QUARTO
                print("=" * 31)
                quantd_desejada = int(input("Quantidade de pessoas : "))
                data_checkin = int(input("Dia do check-in : "))
                data_checkout = int(input("Data do check-out : "))

                a = gera_quartos_disponiveis(reservas, [q1,q2,q3,q4])  # quartos vazios

                b = gera_quartos_disponiveis_jaalugados(reservas, [q1, q2, q3, q4],dias)  # tem que deixar a lista de quartos

                tem_quartos_disponiveis = gera_quartos_disponiveis_pordata(quantd_desejada, data_checkin, data_checkout, a, b)

                if tem_quartos_disponiveis is True:
                    qual_quer = int(input("Digite o numero do quarto escolhido : "))

                    # reservas = [["34", 0, 2], ["12", 1, 1]]
                    if acha_vip_por_id_quarto([q1,q2,q3,q4], qual_quer-1) == 1 and vip == 1:
                        reservas.append([f"{data_checkin}{data_checkout}", id_atual, qual_quer - 1])
                        print(f"O Quarto {qual_quer} foi alugado do dia {data_checkin} ao dia {data_checkout} com sucesso !!")
                    elif acha_vip_por_id_quarto([q1,q2,q3,q4], qual_quer-1) == 1 and vip == 0 :
                        print("\n Desculpe , esse quarto é reservado somente para clientes VIP")
                    else:
                        print(f"O Quarto {qual_quer} foi alugado do dia {data_checkin} ao dia {data_checkout} com sucesso !!")
                        reservas.append([f"{data_checkin}{data_checkout}", id_atual, qual_quer - 1])
                    print("=" * 31)
            elif choice12 == 2:

                acha_reserva_por_id(id_atual, reservas, [q1,q2,q3,q4])


            elif choice12 == 3:
                if vip == 0:
                    print("Desculpe , opcao disponivel somente a clientes vips")
                    break
                if vip == 1:
                    print("=" * 3, "MENU DE ALTERACAO", "=" * 9, )
                    print("O que gostaria de alterar? : ")
                    mudar = int(input((
                                          "[1]Mudar de Quarto \n[2]Mudar data de Check-In \n[3]Mudar data de Check-Out\n[4]Cancelar minha Reserva[0]Sair\nResposta : ")))
                    print("=" * 31)

                    if mudar == 1:
                        print("=" * 3, "MENU DE ALTERACAO", "=" * 9, )
                        print("Quartos disponiveis para a mesma quantidade de pessoas : ")
                        print("OBS : Os quartos a seguir possuem disponibilidade de acordo com\nseu dia de check-in e check-out")

                        reserva_dela = retorna_reserva_por_id(id_atual, reservas, [q1, q2, q3, q4])
                        quantd_desejada =  acha_quantd_por_id_quarto([q1,q2,q3,q4],reserva_dela[1])
                        c = gera_quartos_disponiveis(reservas, [q1, q2, q3, q4])  # quartos vazios
                        d = gera_quartos_disponiveis_jaalugados(reservas, [q1, q2, q3, q4],dias)  # tem que deixar a lista de quartos
                        tem_quartos_disponiveis =  gera_quartos_disponiveis_pordata(quantd_desejada, reserva_dela[0][0], reserva_dela[0][1], c,d)
                        if tem_quartos_disponiveis is True:

                                qual_quer = int(input("Digite o numero do quarto escolhido : "))
                                print(f"O Quarto {qual_quer} foi alugado do dia {reserva_dela[0][0]} ao dia {reserva_dela[0][1]} com sucesso !!")
                                reservas.append([f"{reserva_dela[0][0]}{reserva_dela[0][1]}", id_atual, qual_quer - 1])
                                print(f"A reserva do  Quarto {reserva_dela[1]+1} foi cancelada ")
                                reservas.remove(reserva_dela)
                        print(reservas)
        # cadastra cliente
    elif choice == 2:
            # (self, nome1, idade1, sexo1, vip1, acessos1, id1):
            id_cliente = id_cliente + 1

            nome_novo = input("Nome : ")
            idade_novo = int(input("Idade : "))
            sexo_novo = int(input("Sexo [0]Homem [1]Mulher : "))
            sexo_novo = check(0, 1, sexo_novo)
            vip_novo = int(input("Gostaria de ser um cliente VIP? [0]Nao [1]Sim "))
            vip_novo = check(0, 1, vip_novo)
            if vip_novo == 0:
                print(
                    "Gostaria de algum adicionar ? \n[1]Open bar \n[2]Acesso a todos os restaurantes \n[3]Acesso aos shows")
                codigo1 = int(input("Acesso ao Open bar      [0]Nao [1]Sim"))
                codigo1 = check(0, 1, codigo1)
                codigo2 = int(input("Acesso aos restaurantes [0]Nao [1]Sim"))
                codigo2 = check(0, 1, codigo2)
                codigo3 = int(input("Acesso aos shows        [0]Nao [1]Sim"))
                codigo3 = check(0, 1, codigo3)

                acessos_novo = f"{codigo1}" + f"{codigo2}" + f"{codigo3}"
                a = Cliente(nome_novo, idade_novo, sexo_novo, vip_novo, acessos_novo, id_cliente)
                print(f"O cliente de {nome_novo} foi adicionado a lista com id {id_cliente}")
                clientes.append(a)

            else:
                acessos_novo = "111"
                a = VIP(nome_novo, idade_novo, sexo_novo, vip_novo, acessos_novo, id_cliente)
                print(f"O cliente vip de {nome_novo} foi adicionado a lista com id {id_cliente}")
                clientes.append(a)

                break
                break

print(clientes)

