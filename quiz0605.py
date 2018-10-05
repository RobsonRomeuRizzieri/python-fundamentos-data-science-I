# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def medianExemplo(a,b,c):
    if (a >= b and a <= c) or (a >= c and a <= b):
        return a
    if (b >= c and b <= a) or (b >= a and b <= c):
        return b
    if (c >= b and c <= a) or (c >= a and c <= b):
        return c
    
def median(a,b,c):   
    #retorna o maior número dos três 
    big = biggest(a, b, c)
    #Se maior for o número da variavel a
    if big == a:
        # retorna o maior de b e c, tendo assim o mediano dos três número
        return bigger(b,c)
    #Se o maior não foi a mas sim b 
    if big == b:
        #procura o maior entre a e c, tendo assim o mediano dos três número
        return bigger(a,c)
    #Se não foi nem a e nem b só pode ser o C o maior número    
    else:
        #então procuramos o maior entre a e b, tendo assim o mediano dos três números
        return bigger(a,b)

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7







