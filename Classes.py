#Classe para um cliente normal
class Cliente:

    def __init__(self, nome1, idade1, sexo1,vip1,acessos1,id1):
        self.nome = nome1
        self.idade = idade1
        self.sexo = sexo1
        self.vip = vip1
        self.acessos = acessos1
        self.id = id1

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def get_sexo(self):
        return self.sexo

    def set_sexo(self, sexo1):
        self.sexo = sexo1

    def get_vip(self):
            return self.vip

    def get_acessos(self):
        return self.acessos

    def get_id(self):
        return self.id


#Classe para o cliente VIP
class VIP(Cliente):
    def __init__(self, nome1, idade1, sexo1,vip1,acessos1,id1):
        super().__init__(nome1, idade1, sexo1,vip1,acessos1,id1) # o que o cliente vip tem a mais de atributo ?

#Classe para o quarto normal
class Quarto:

    def __init__(self,quantd1 , camas1, andar1, varanda1,id1):
        self.quantd_pessoas = quantd1
        self.quand_camas = camas1
        self.andar = andar1
        self.varanda = varanda1
        self.camas = ""
        self.id = id1

    def get_camas(self):
        return self.quand_camas

    def get_andar1(self):
        return self.andar

    def get_varanda(self):
        return self.varanda

    def get_id(self):
        return self.id

    def get_reserva(self):
        print(f"Data da reserva : 00/00/00")
        print(f"Fim da reserva : 00/00/00")
        if self.varanda == 1:
            print(f"Tipo de quarto : Standart , com varanda, {self.andar} andar")
        else:
            print(f"Tipo de quarto : Standart , sem varanda, {self.andar} andar")
        self.camas = f"{self.quand_camas[0]} cama(s) de solteiro / {self.quand_camas[2]} camas(s) de casal"
        print(f"Caracteristicas : {self.camas}")
        print(f"Andar : {self.andar}")


#Classe para o quarto VIP
class QuartoVIP(Quarto):
    def __init__(self,quantd1 , camas1, andar1, varanda1,id1,pne1,tematico1):
        super().__init__(quantd1 , camas1, andar1, varanda1,id1)
        self.pne = pne1
        self.tematico = tematico1

    def get_pne(self):
        return self.pne

    def get_tematico(self):
        return self.tematico

    def get_reserva(self):
        print(f"Data da reserva : 00/00/00")
        print(f"Fim da reserva : 00/00/00")
        if self.pne == 1 :
            print(f"Quarto adptado para pessoas com necessidades especiais")
        if self.tematico == 1 :
            print("Quarto tematico ")
        print(f"Tipo de quarto : Premium , com varanda e suite , {self.andar} andar")
        self.camas = f"{self.quand_camas[0]} cama(s) de solteiro / {self.quand_camas[2]} camas(s) de casal"
        print(f"Caracteristicas : {self.camas}")
        print(f"Andar : {self.andar}")

