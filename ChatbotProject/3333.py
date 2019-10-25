# Travis Morrow
while True:
    fname = input('What is your first name? ' )
    lname = input('What is your last name? ' )
    time = input('What time of day is it (Morning, Afternoon, Evening): ' ) 
    greeting = 'Have a good'

    if time == 'Morning':
        print(greeting, 'breakfast', fname, lname[0:])
        break
    if time == 'Afternoon' 
        time = 'lunch,'
        break
    if time == 'Evening':
        time = 'dinner,'
        break
    else:
        time = 'one,'
        break

new_greeting = print("{0} {1} {2} {3}".format(greeting, time, fname, lname[:1]))
    
another = input('Would you like another greeting? ')
count = 0
if another[0] == 'y':
    #print('??????????????????')
if another[0] != 'y':
    count = count + 1
    print('You received {} greetings'.format(count)) 