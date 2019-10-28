#   open mbox-short.txt, transform to uppercase
#CC4-Ex08
work = open('mbox-short.txt')
for line in work:
    line = line.upper().rstrip()
    print(line)