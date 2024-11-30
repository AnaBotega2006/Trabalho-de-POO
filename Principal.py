from Classes import *
from ObjetosPessoas import *

#listas de controle


#variaveis
#id_cliente = len(clientes)-1
#codigo = ""

choice = 1


while choice != 0:
    print("=" * 3 , "OPCOES" ,"=" * 20 , )
    print("Já é nosso cliente ? \n[1] Sim \n[2] Nao , quero me casdastrar \n[0] Sair ")
    choice = int(input("Resposta : "))
    print("="*31)

    if choice == 1 : #Se ja for cliente
        pass

    elif choice == 2: # cadastra cliente
        while choice != 0:
            # (self, nome1, idade1, sexo1, vip1, acessos1, id1):
            id_cliente = id_cliente + 1

            nome_novo = input("Nome : ")
            idade_novo = int(input("Idade : "))
            sexo_novo = int(input("Sexo [0]Homem [1]Mulher : "))
            vip_novo = int(input("Gostaria de ser um cliente VIP? [0]Nao [1]Sim "))
            if vip_novo == 0 :
                print("Gostaria de algum adicionar ? \n[1]Open bar \n[2]Acesso a todos os restaurantes \n[3]Acesso aos shows")
                codigo1 = int(input("Acesso ao Open bar      [0]Nao [1]Sim"))
                codigo2 = int(input("Acesso aos restaurantes [0]Nao [1]Sim"))
                codigo3 = int(input("Acesso aos shows        [0]Nao [1]Sim"))
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


