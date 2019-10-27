#   open alice.txt, count the lines, and
#   print out number of lines
#CC4-Ex05
with open('alice.txt', 'r') as file:
    count = 0
    for lines in file:
        count = count + 1
print('Line count: ' + str(count))
    
