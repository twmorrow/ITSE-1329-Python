work = input('Enter the file name: ')
try:
    mwork = open(work)
except:
    #work = work.upper()
    print(work, "TO YOU - You have been punk'd")
    quit()
count = 0
for line in mwork:
    if line.startswith('Subject'):
        count = count + 1
print('There were', count, 'subject lines in', work)