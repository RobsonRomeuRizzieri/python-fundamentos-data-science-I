# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'



def is_friend(nome):
    primeira_letra = nome[0:1]
    #print primeira_letra
    return  primeira_letra.lower() == 'D'.lower()


print is_friend('Diane')
#>>> True

print is_friend('Fred')
#>>> False