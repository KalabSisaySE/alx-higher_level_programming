#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    type = "negative"
elif number == 0:
    type = "zero"
else:
    type = "positive"
    
print(f"{number} is {type}")
