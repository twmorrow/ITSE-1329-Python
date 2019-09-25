hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    if float(hours) <= 40:
        pay = float(hours) * float(rate)
    elif float(hours) > 40:
        pay = ((float(hours)-40) * float(rate) * 1.5) + float(rate) *40
    print("Pay:", pay) 
except:
    print('Error, please enter numeric input')
quit()