#CC4-Ex02
# Define function called random_turtle
def random_turtle():
    answer = turtle.randint(1,10)
    return answer
# Import the random module as turtle:
import random as turtle
# Use randint to produce a random integer between 
# 1 and 10 and save it to a variable called answer
print(random_turtle())