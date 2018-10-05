# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    maiorNumero = 0
    for item in list_of_numbers:
        if item > maiorNumero:
            maiorNumero = item
    return maiorNumero


print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
