from Classes import *
from listas import *



def acha_nome_por_id(id_achar,clientes):
    for pessoa in clientes :
        if pessoa.get_id() == id_achar :
            return pessoa.nome
def acha_reserva_por_id(id_achar,reservas,quartos):
    for reserva in reservas :
        if reserva[0] == id_achar:
            for quarto in quartos:
                if reserva[1] == quarto.get_id():
                    quarto.get_reserva()


