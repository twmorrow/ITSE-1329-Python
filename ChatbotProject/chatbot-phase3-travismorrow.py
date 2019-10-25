# Travis Morrow
def greeter(time):
    """This function....."""
    if time == 'Morning':
        return 'Have a good ' + 'breakfast, ' + fname + ' ' + lname[:1]  
    elif time == 'Afternoon':
        return 'Have a good ' + 'lunch, ' + fname + ' ' + lname[:1] 
    elif time == 'Evening':
        return 'Have a good ' + 'dinner, ' + fname + ' ' + lname[:1] 
    else: 
        return 'Have a good ' + 'one, ' + fname + ' ' + lname[:1] 
count = 0
while True:
    fname = input('What is your first name? ' )
    lname = input('What is your last name? ' )
    time = input('What time of day is it (Morning, Afternoon, Evening): ' )  
    greeting = 'Have a good'

    #new_greeting = print("{0} {1} {2} {3}".format(greeting, time, fname, lname[:1]))
    print(greeter(time))
    another = input('Would you like another greeting? ')
    count = count + 1
    if another == 'no':
        break
print('You received {0} greetings'.format(count))