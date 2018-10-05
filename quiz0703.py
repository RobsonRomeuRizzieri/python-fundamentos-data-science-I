# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def menor(a,b):
    if a < b:
        return a
    else:
        return b

def set_range(a,b,c):
    # Your code here
    big = biggest(a, b, c)
    if big == a:
        menor_valor = menor(b,c)
    if big == b:
        menor_valor = menor(a,c)
    else:
        menor_valor = menor(a,b)
    return big - menor_valor

print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6