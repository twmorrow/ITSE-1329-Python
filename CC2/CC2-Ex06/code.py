
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

else :
    print('Bad Score')
    
#elif float(s) <= 0."9print('B')
    
#>=0.8 	B
#>=0.7 	C
#>=0.6 	D
#<0.6 	F
