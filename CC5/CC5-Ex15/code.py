#CC5-Ex15
def pet_names(names):
    counts = dict() # This is another way to create an empty dictionary
    for name in names:
        counts[name] = counts.get(name, 0) + 1
    return counts
print(pet_names(['fido', 'bob', 'joe', 'fido', 'fido']))
