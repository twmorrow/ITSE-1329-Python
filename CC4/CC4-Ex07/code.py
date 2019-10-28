#   open alice.txt, print lines that startwith
#   'Alice' and print out result with right-hand whitespace
#   removed
#CC4-Ex07
work = open('alice.txt')
for line in work:
    line = line.rstrip()
    if line.startswith('Alice'):
        print(line)