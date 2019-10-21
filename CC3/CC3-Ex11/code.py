def first_two(string):
    if len(string) < 2:
        return("String is too short")
    elif len(string) >= 2:
        return (string[0:2])
    
print(first_two('n'))