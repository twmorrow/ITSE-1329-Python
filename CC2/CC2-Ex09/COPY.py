hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = float(hours) * float(rate)
opay = pay * 40 + 1.5
try:
    if float(hours) <= 40:
        print("Pay:", pay)  
    if float(hours) >40:
        print("Pay:", opay)
except:
    print('Error, please enter numeric input')