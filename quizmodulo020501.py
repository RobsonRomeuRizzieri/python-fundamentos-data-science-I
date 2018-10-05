def hours2days(horas):
    #pega o valor inteiro da divisão
    dias = horas // 24
    #horas = horas - (dias * 24)
    #ou poderia pegar o resto da divisão
    horas = horas % 24
    #Lista com os valores fixos
    diasHoras = (dias, horas)
    return diasHoras
print(hours2days(24)) # 24 horas é um dia e zero horas
#(1, 0)
print(hours2days(25)) # 25 horas é um dia e uma hora
#(1, 1)
print(hours2days(10000))
#(416, 16)