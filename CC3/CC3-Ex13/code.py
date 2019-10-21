#CC3_Ex13
def not_string(string):
    for word in string:
        if (string[0:3]) == 'not':
            return (string)
        else:
            return ('not ' + (string))
            
#print(not_string('bananas'))