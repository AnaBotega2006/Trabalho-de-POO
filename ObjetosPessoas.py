from Classes import *

c1 = Cliente("Paulo",40 , 0 , 0 , "000",0)
Cliente("Neusa",34 , 1 , 0 , "110",1)
VIP("Joana",40 , 1 , 1 , "111",2)



c1 = Cliente("Paulo",40 , 0 , 0 , "000",0)
q1 = Quarto(4, "2C0S", 1, 1,0)

c2 = Cliente("Neusa",34 , 1 , 0 , "110",1)
q2 = Quarto(1, "1S0S", 2, 0,1)


c3 = Cliente("Leandro",18 , 0 , 0 , "000",2)
q3 = Quarto(2, "1C0S", 3, 0,2)


c4 = VIP("Joana",40 , 1 , 1 , "111",3)
q4 = QuartoVIP(4 , "1C2S", 4, 1,3,1,0)

#Paulo id 0 tem o quarto 3 id 2
#Neusa id 1 tem o quarto 2 id 1
#Leandro id 2 tem o quarto 1 id 0
#Joana id 3 tem o quarto 4 id 3

#reservas = [[0,2][1,1],[2,0],[3,3]]


