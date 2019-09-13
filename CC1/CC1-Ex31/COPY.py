str = 'X-DSPAM-Confidence:0.8475'
zen = str.find(':') 
#print(zen)

zen_a = str[zen+1:50]
print(float(zen_a))
#print(zen_a)