# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.
def weekend(day):
    return 'saturday' == day.lower() or 'sunday' == day.lower()
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False