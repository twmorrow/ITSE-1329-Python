#   open mbox-short.txt, print lines that startwith
#   From: and print out result with right-hand whitespace
#   removed
#CC4-Ex06
work = open('mbox-short.txt')
for lines in work:
    lines = lines.rstrip()
    if lines.startswith('From:'):
        print(lines)
    