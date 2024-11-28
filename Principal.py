choice = 1




while choice != 0:
    print("=" * 3 , "OPCOES" ,"=" * 20 , )
    print("Já é nosso cliente ? \n[1] Sim \n[2] Nao \n[0] Sair ")
    choice = int(input("Resposta : "))
    print("="*31)

    if choice == 1 :
        while choice != 0:
            print("=" * 3, "OPCOES DO CLIENTE", "=" * 9, )
            print("Bem vindo novamente! \n[1] Consultar minha reserva \n[2] Alterar minha reserva \n[3]Fazer consumo no Hotel ")
            choice = int(input("Resposta : "))
            print("=" * 31)
    elif choice == 2:
        print("=" * 3, "OPCOES", "=" * 20, )
        print("Já é nosso cliente ? \n[1] Sim \n[2] Nao ")
        choice = int(input("Resposta : "))
        print("=" * 31)

    else:
        break



