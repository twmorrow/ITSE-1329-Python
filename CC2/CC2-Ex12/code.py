#try :
s = input('Enter Score: ')
if float(s) < 0.60:
        print('F')
elif float(s) < 0.70:
        print('D')
elif float(s) < 0.80:
        print('C')
elif float(s) < 0.90:
        print('B')
elif float(s) <= 1.00:
        print('A')
elif float(s) > 1.00:
    print('Bad score')
else:
    print('Please enter numeric input')
quit()