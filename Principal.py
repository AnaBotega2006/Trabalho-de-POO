from Classes import *
from ObjetosPessoas import *
from Funcoes import *

#LISTAS DE CONTROLE

clientes = [c1,c2,c3,c4,c5,c6,c7,c8]
quartos = [q1,q2,q3,q4,q5,q6,q7,q8]
quartos_alugados = []
dias = [1,2,3,4,5,6,7,8,9]
reservas = [["34",0,2,0],["12",1,1,0],["14",3,3,0]]


#VARIÁVEIS
id_cliente = len(clientes) - 1
codigo = ""
primeira_vez = 0
choice12 = 1000

choice = 1

while choice != 0:
    print("=" * 3, "OPCOES", "=" * 20, )
    print("Já é nosso cliente ? \n[1] Sim \n[2] Nao , quero me casdastrar \n[3] Consultar estatísticas do hotel\n[0] Sair ")
    choice = int(input("Resposta : "))
    choice = check(0, 3, choice)
    primeira_vez = 0
    print("=" * 31)

    #LOGIN DO CLIENTE
    if choice == 1:
        while choice12 != 0:
            if primeira_vez == 0:
                
                id_atual = int(input("Digite seu ID :"))
                vip = acha_vip_por_id(id_atual,clientes)

                nome = acha_nome_por_id(id_atual,clientes)

                if nome == False:
                    print("Não encontramos esse ID no nosso sistema. \n Cadastre-se no nosso site ou tente outro ID.")
                    break
                else:
                    print(f"Bem vindo novamente {nome}!\n[1]Alugar Quarto \n[2] Consultar minha reserva \n[3] Alterar minha reserva(exclusivo VIP) \n[4]Fazer consumo no Hotel \n[5]Fatura \n[6]Consultar meus dados \n \n[0]Sair\n ")
                    choice12 = int(input("Resposta : "))
                    choice12 = check(0,6,choice12)
                    primeira_vez = 1
            else :
                print("=" * 31)
                print( f"[1]Alugar Quarto \n[2] Consultar minha reserva \n[3] Alterar minha reserva(exclusivo VIP) \n[4]Fazer consumo no Hotel \n[6]Consultar meus dados \n[5]Fatura \n \n[0]Sair\n ")
                choice12 = int(input("Resposta : "))
                choice12 = check(0,6,choice12)

            print("=" * 31)

            #ALUGAR QUARTO
            if choice12 == 1:
                print("=" * 31)
                quantd_desejada = int(input("Quantidade de pessoas : "))
                data_checkin = int(input("Dia do check-in : "))
                data_checkout = int(input("Data do check-out : "))

                a = gera_quartos_disponiveis(reservas, [q1,q2,q3,q4,q5,q6,q7,q8])  # quartos vazios

                b = gera_quartos_disponiveis_jaalugados(reservas, [q1,q2,q3,q4,q5,q6,q7,q8],dias)  # tem que deixar a lista de quartos

                tem_quartos_disponiveis = gera_quartos_disponiveis_pordata(quantd_desejada, data_checkin, data_checkout, a, b)

                if tem_quartos_disponiveis is True:
                    qual_quer = int(input("Digite o numero do quarto escolhido : "))

                    # reservas = [["34", 0, 2], ["12", 1, 1]]
                    if acha_vip_por_id_quarto([q1,q2,q3,q4,q5,q6,q7,q8], qual_quer-1) == 1 and vip == 1:
                        reservas.append([f"{data_checkin}{data_checkout}", id_atual, qual_quer - 1,0])
                        print(f"O Quarto {qual_quer} foi alugado do dia {data_checkin} ao dia {data_checkout} com sucesso !!")
                    elif acha_vip_por_id_quarto([q1,q2,q3,q4,q5,q6,q7,q8], qual_quer-1) == 1 and vip == 0 :
                        print("\n Desculpe , esse quarto é reservado somente para clientes VIP")
                    else:
                        print(f"O Quarto {qual_quer} foi alugado do dia {data_checkin} ao dia {data_checkout} com sucesso !!")
                        reservas.append([f"{data_checkin}{data_checkout}", id_atual, qual_quer - 1,0])
                    print("=" * 31)
            
            #CONSULTAR RESERVA
            elif choice12 == 2:
                print("Suas reservas, se tiver:")
                acha_reserva_por_id(id_atual, reservas, [q1,q2,q3,q4,q5,q6,q7,q8])

            #ALTERAR RESERVA
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

                        reserva_dela = retorna_reserva_por_id(id_atual, reservas, [q1,q2,q3,q4,q5,q6,q7,q8])
                        quantd_desejada =  acha_quantd_por_id_quarto([q1,q2,q3,q4,q5,q6,q7,q8],reserva_dela[1])
                        c = gera_quartos_disponiveis(reservas, [q1,q2,q3,q4,q5,q6,q7,q8])  # quartos vazios
                        d = gera_quartos_disponiveis_jaalugados(reservas, [q1,q2,q3,q4,q5,q6,q7,q8],dias)  # tem que deixar a lista de quartos
                        tem_quartos_disponiveis =  gera_quartos_disponiveis_pordata(quantd_desejada, reserva_dela[0][0], reserva_dela[0][1], c,d)
                        if tem_quartos_disponiveis is True:

                                qual_quer = int(input("Digite o numero do quarto escolhido : "))
                                print(f"O Quarto {qual_quer} foi alugado do dia {reserva_dela[0][0]} ao dia {reserva_dela[0][1]} com sucesso !!")
                                reservas.append([f"{reserva_dela[0][0]}{reserva_dela[0][1]}", id_atual, qual_quer - 1])
                                print(f"A reserva do  Quarto {reserva_dela[1]+1} foi cancelada ")
                                reservas.remove(reserva_dela)
                        print(reservas)
            
            #FAZER CONSUMO 
            elif choice12 == 4: 
                for c in clientes : 
                    if id_atual == c.get_id():
                        acessos = c.get_acessos()
                        open_bar = int(acessos[0])
                        restaurante = int(acessos[1])
                        shows = int(acessos[2])

                        if open_bar == 1 : 
                            print("Voce já tem acesso ao Open-Bar ")

                        else:
                            choice4= 1
                            while choice4 != 0 : 
                                print("\nVocê deseja consumir algo no bar?")
                                choice4 = int(input("opçõs de consumo \n [1] agua R$ 2,00\n [2] coca R$ 3,00 \n [3] chips R$ 4,00 \n [0] nenhum \n resposta:" ))
                                reserva_dela = retorna_reserva_por_id(id_atual,reservas,quartos)
                                if choice4 == 1:
                                    reserva_dela[3] += 2
                                    print(f"Seu consumo atual é de: R$ {reserva_dela[3]},00")
                                
                                if choice4 == 2:
                                    reserva_dela[3] += 3
                                    print(f"Seu consumo atual é de: R$ {reserva_dela[3]},00")
                                
                                if choice4 == 3:
                                    reserva_dela[3] += 4  
                                    print(f"Seu consumo atual é de: R$ {reserva_dela[3]},00")                  

                        
                        if restaurante == 1 :
                            print("Voce já tem acesso aos Restaurantes ")
                        else:
                            choice4= 1
                            while choice4 != 0 : 
                                print("\nVocê deseja consumir algo no restaurante?")
                                choice4 = int(input("opçõs de consumo \n [1] Cafe da manha R$ 20,00\n [2] Almoco R$ 30,00 \n [3] Janta R$ 30,00 \n [0] nenhum \n resposta:" ))
                                if choice4 != 0:
                                    print("Obs : por pessoa ")
                                    quantd = int(input("Quantidade de refeicoes : "))
                                    reserva_dela = retorna_reserva_por_id(id_atual,reservas,quartos)

                                if choice4 == 1:
                                    reserva_dela[3] += 20 * quantd
                                    print(f"Seu consumo atual é de: R$ {reserva_dela[3]},00")
                                
                                if choice4 == 2:
                                    reserva_dela[3] += 30 * quantd
                                    print(f"Seu consumo atual é de: R$ {reserva_dela[3]},00")
                                
                                if choice4 == 3:
                                    reserva_dela[3] += 30 * quantd 
                                    print(f"Seu consumo atual é de: R$ {reserva_dela[3]},00")


                        if shows == 1 :
                            print("Voce já tem acesso aos Shows ")
                            


                        else:
                            print("\nDeseja comprar ingressos para o show EXCALIBUR ?")
                            choice4 = int(input("R$ 50,00 cada ingresso \nQuantidade:" ))
                            reserva_dela[3] += 50 * choice4
                            print(f"Seu consumo atual é de: R$ {reserva_dela[3]},00")


                        #COMPLETAR 

            #FATURA
            if choice12 == 5:
                for reserva in reservas : 
                    if reserva[1] == id_atual:
                        retorna_fatura(id_atual,reservas,clientes,reserva)
            
            #CONSULTA/ALTERA DADOS CLIENTE
            if choice12 == 6:
                print("Consulta de dados")
                for c in clientes : 
                    if id_atual == c.get_id():
                        print("Seu nome é:", c.get_nome())
                        print("Sua idade é:", c.get_idade())
                        if c.get_sexo() == 1:
                            print("Seu sexo é: F")
                        else:
                            print("Seu sexo é: M")

                        print("\n Deseja alterar seus dados? \n[1] Sim \n[2] Não \n[3]Desejo apagar meu cadastro")
                        q = int(input("Resposta: "))

                        if q == 1:
                            nome_novo = input("Nome : ")
                            idade_novo = int(input("Idade : "))
                            sexo_novo = int(input("Sexo [0]Homem [1]Mulher : "))
                            sexo_novo = check(0, 1, sexo_novo)

                            c.set_nome(nome_novo)
                            c.set_idade(idade_novo)
                            c.set_sexo(sexo_novo)

                            print("Informações do cliente atualizadas com sucesso!")
                        
                        elif q == 3:
                            reserva_dela = retorna_reserva_por_id(id_atual, reservas, [q1,q2,q3,q4,q5,q6,q7,q8])
                            count = 0
                            clientes.remove(c)

                            reservas.remove(reserva_dela)

                            print("Seu cadastro foi removido com sucesso")
                break
                                

                            

    
                



    #CADASTRA CLIENTE NOVO
    elif choice == 2:
            # (self, nome1, idade1, sexo1, vip1, acessos1, id1)
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

                #break
                #break
    
    elif choice == 3:
        print("Porcentagem dos clientes que são mulheres: ", est_sexo(clientes), "%")
        print("Idade média dos clientes do hotel: ", est_idade(clientes), "anos de idade")



