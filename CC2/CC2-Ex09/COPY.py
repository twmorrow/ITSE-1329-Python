s = input('Enter Score: ')
try:
    if float(s) < 0.60:
        print('F')
    if float(s) < 0.70:
        print('D')
    if float(s) < 0.80:
        print('C')
    if float(s) < 0.90:
        print('B')
    if float(s) <= 1.00:
        print('A')
    if float(s) > 1.00:
        print('Bad score')
except:
    print('Please enter numeric input')
quit()