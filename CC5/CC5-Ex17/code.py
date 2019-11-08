#CC5-Ex17
def pet_nums(pets):
    counts = dict()
    for animal in pets:
       counts[animal] = counts.get(animal, 0) + 1
    return counts
print(pet_nums(['cat', 'cat', 'cat', 'dog']))