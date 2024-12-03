from Classes import *
from ObjetosPessoas import *

def acha_quantd_por_id_quarto(quartos,id):
    for quarto in quartos :
        if quarto.get_id() == id :
            return quarto.quantd_pessoas

def acha_vip_por_id_quarto(quartos, id):
    for quarto in quartos :
        if quarto.get_id() == id :
            return quarto.get_vip()

def acha_nome_por_id(id_achar,clientes):
    verifica = 0
    for pessoa in clientes :
        if pessoa.get_id() == id_achar :
            verifica = 1
            return pessoa.nome    
    if verifica == 0:
        return False

def retorna_reserva_por_id(id_achar,reservas,quartos):
    for reserva in reservas :
        if reserva[1] == id_achar:
            return reserva
    for quarto in quartos :
        if quarto.get_id() == id :
            return quarto.get_vip()

def acha_reserva_por_id(id_achar,reservas,quartos):
    for reserva in reservas :
        if reserva[1] == id_achar:
            for quarto in quartos:
                if reserva[2] == quarto.get_id():
                    quarto.get_reserva(reserva[0])

def acha_vip_por_id(id_achar,clientes):
    for pessoa in clientes :
        if pessoa.get_id() == id_achar :
            return pessoa.vip
            
def get_info_por_id(id_achar,quartos):
    for quarto in quartos :
        if quarto.get_id() == id :
            return quarto.get_info()

def gera_quartos_disponiveis(reservas,quartos):
    #reservas = [["34",0,2],["34",1,1]]
    quartos_vazios = quartos
    for reserva in reservas :
        for quarto in quartos:
            if reserva[2] == quarto.get_id() :
                quartos_vazios.remove(quarto)
    return quartos_vazios

def gera_quartos_disponiveis_jaalugados(reservas, quartos, dias):
    #tem que botar um range aqui dois numeros da certo mas 1 a 4 da errado ele retorna 2 e 3 mas nao esta disponivel no 2 e 3
    quarto_vazio_limitado = []
    for reserva in reservas:
        livre = dias.copy()  # [1,2,3,4]
        for dia in dias:  # 1 , 2 , 3 , 4
            # reservas = [["34",0,2],["12",1,1]]
            if int(reserva[0][0]) == dia:
                livre.remove(dia)  # [1,2,4]
            if int(reserva[0][1]) == dia:
                livre.remove(dia)  # [1,2]
        for quarto in quartos:  # [1,2] #quartos = [q1,q2,q3,q4]
            if reserva[2] == quarto.get_id():
                # [f"{livre[0]}{livre[1]}", quartos.get_id()]
                quarto_vazio_limitado.append([f"{livre[0]}{livre[1]}", quarto.get_id()])
    return quarto_vazio_limitado


def gera_quartos_disponiveis_pordata(quantd_desejada,data_checkin,data_checkout,quartos_vazios,quarto_vazio_limitado):

    for quarto in quartos_vazios: # esta ok para quantidade
        count = 0
        if quarto.get_quantd() == quantd_desejada:
            if acha_vip_por_id_quarto([q1, q2, q3, q4], quarto.get_id()):
                count += 1
                print(f"Quarto (VIP) {quarto.get_id()+1}\t disponivel ")
                get_info_por_id(quarto.get_id(),[q1,q2,q3,q4])
            else :
                count += 1
                print(f"Quarto {quarto.get_id() + 1}\t disponivel ")
                get_info_por_id(quarto.get_id(),)

    for quarto in quarto_vazio_limitado:

            #quartos2 = [['12', 2], ['34', 1]]
            acha_quantd_por_id_quarto([q1,q2,q3,q4], quarto[1])

            quarto1dig = int(quarto[0][0])
            quarto2dig = int(quarto[0][1])
            quartoid = int(quarto[1])
            if acha_quantd_por_id_quarto([q1, q2, q3, q4], quartoid) >= quantd_desejada:

                if data_checkin in range (quarto1dig,quarto2dig + 1) and data_checkout in range (quarto1dig,quarto2dig+1) :
                    if acha_vip_por_id_quarto([q1, q2, q3, q4], quartoid) == 1 :
                        print(f"Quarto (VIP){int(quarto[1]) + 1}\t disponivel somente do dia {quarto[0][0]} ao dia {quarto[0][1]} ")
                        get_info_por_id(quartoid,[q1,q2,q3,q4])
                        count += 1
                    else :
                        print(f"Quarto {int(quarto[1]) + 1}\t disponivel somente do dia {quarto[0][0]} ao dia {quarto[0][1]} ")
                        get_info_por_id(quartoid,[q1,q2,q3,q4])
                        count += 1
    if count == 0:
        print("Não temos quartos disponiveis nessas condicoes ")
        return False
    else :
        return True


def retorna_fatura(id_atual,reservas,clientes,reserva_dela1):
    fatura = 0
    fatura2 = 0 
    f_total = 0 
    for cliente in clientes : 
        if cliente.get_id() == id_atual:
            acessos = cliente.get_acessos()
            reserva_dela = reserva_dela1
            vip = acha_vip_por_id_quarto([q1,q2,q3,q4], reserva_dela[2])

            if vip == 0 : #se o quarto nao for vip o preco e 100 por dia (dia vem do range)
                for dia in range (int(reserva_dela[0][0]),int(reserva_dela[0][1])+ 1): 
                    fatura = fatura + 100 
            else :
                for dia in range (int(reserva_dela[0][0]),int(reserva_dela[0][1])+ 1): 
                    fatura = fatura + 200 
    print(f"Por {reserva_dela[0][1]} dias no quarto : R${fatura},00")
    for beneficio in acessos:
        if beneficio == 1: 
            fatura2 = fatura2 + 150
    print(f"Por {acessos.count("1")} beneficios comprados: R${fatura2},00")
    f_total = fatura + fatura2 + reserva_dela[3]
    print(f"No total(diaria + consumos + beneficios) voce deve pagar : R${f_total},00")


#função checagem intervalo fechado
def check (minimo,maximo,numero):
    while ( (numero<minimo) or (numero > maximo) ):
        print("Número fora dos parâmetros aceitos")
        numero = int(input("Por favor digite novamente: "))
    return numero


#ESTATÍSTICAS

#porcentagem de mulheres
def est_sexo (clientes):
    soma = 0
    for pessoa in clientes :
        soma += pessoa.get_sexo()
    total = (soma / len(clientes) ) *100
    return total # de mulheres, em porcentagem

#porcentagem de quartos ocupados FALTA TERMINAR
def est_quartos(reservas, quartos):
    quartos_vazios = len(gera_quartos_disponiveis(reservas,quartos))
    quartos_ocupados = len(quartos) - quartos_vazios
    total = (quartos_ocupados / len(quartos) ) *100
    return total

# idade media dos clientes do hotel
def est_idade(clientes):
    soma = 0
    for pessoa in clientes :
        soma += pessoa.get_idade()
    total = (soma / len(clientes) )
    return total
