# Travis Morrow
count = 1
while True:
    fname = input('What is your first name? ' )
    lname = input('What is your last name? ' )
    time = input('What time of day is it (Morning, Afternoon, Evening): ' )  
    greeting = 'Have a good'
    if time == 'Morning':
        time = 'breakfast,'
    elif time == 'Afternoon':
        time = 'lunch,'
    elif time == 'Evening':
        time = 'dinner,'
    else: 
        time = 'one,'
    new_greeting = print("{0} {1} {2} {3}".format(greeting, time, fname, lname[:1]))
    another = input('Would you like another greeting? ')
    if another == 'yes':
        count = count + 1
        print(count)
        continue
    if another == 'no':
        break
print('You received {0} greetings'.format(count))
