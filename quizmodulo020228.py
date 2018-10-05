# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

# Não é obrigado a dar return porque a referencia é a mesma
def union(arr1, arr2):
    arr3 = arr1
    for item in arr2:
        if item not in arr1:
            arr3.append(item)
    return arr3
#Nesse caso vamos atualizar o valor de a que recemos como parametro no arr1 
def union2(arr1, arr2):
    for item in arr2:
        if item not in arr1:
            arr1.append(item)  

# To test, uncomment all lines 
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]
