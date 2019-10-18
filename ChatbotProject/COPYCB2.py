# Travis
fname = input('What is your first name? ' )
lname = input('What is your last name? ' )
time = input('What time of day is it (Morning, Afternoon, Evening): ' )  

greeting = 'Good'
#new_greeting = greeting+time+fname+lname[:1]
new_greeting = print("{0} {1} {2} {3}".format(greeting, time, fname, lname[:1]))
#print(new_greeting)