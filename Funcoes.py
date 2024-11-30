from Classes import *
from listas import *



def acha_nome_por_id(id_achar,clientes):
    for pessoa in clientes :
        if pessoa.get_id() == id_achar :
            return pessoa.nome
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

def gera_quartos_disponiveis(reservas,quartos):
    #reservas = [["34",0,2],["34",1,1]]
    quartos_vazios = quartos
    for reserva in reservas :
        for quarto in quartos:
            if reserva[2] == quarto.get_id() :
                quartos_vazios.remove(quarto)
    return quartos_vazios

def gera_quartos_disponiveis_jaalugados(reservas,quartos,dias):
    quarto_vazio_limitado = []
    for reserva in reservas:
        livre = dias
        for dia in dias: # 1 , 2 , 3 , 4
            # reservas = [["34",0,2],["12",1,1]]
            if int(reserva[0][0]) == dia:
                livre.remove(dia)
            if int(reserva[0][1]) == dia:
                livre.remove(dia)
        for quarto in quartos:
            if reserva[2] == quarto.get_id():
                #[f"{livre[0]}{livre[1]}", quartos.get_id()]
                quarto_vazio_limitado.append( ["bla"])

    return quarto_vazio_limitado


def gera_quartos_disponiveis_pordata(quantd_desejada,data_checkin,data_checkout,quartos_vazios,quarto_vazio_limitado):
    for quarto in quartos_vazios:
        print(f"Quarto {quarto.get_id()+1}\t disponivel do dia 1 ao dia 4 ")
    print(quarto_vazio_limitado)
    for quarto1 in quarto_vazio_limitado:
        print(f"Quarto {quarto1[1].get_id() + 1}\t disponivel do dia {quarto1[0][0]} ao dia {quarto1[0][1]} ")



