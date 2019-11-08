def count_colors(colors):
    counts = dict()  # Create a blank dictionary called counts
    for color in colors:
        counts[color] = counts.get(color, 0) + 1  # Fill in blank
    return counts
print(count_colors(['red', 'blue', 'red', 'white', 'blue', 'red']))