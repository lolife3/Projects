"""
import random

array = [random.randint(0, 50000) for _ in range(15000)]
print(array)

for number in array:
    if 300 < number < 370:
        print(number)        
"""


with open("result.txt", "w") as file:
    for x in range(1, 20000):
        if (x % 5 == 0) * (x % 3 == 0):
            file.write("fizzbuzz!\n")
            continue
            
        elif (x % 5 == 0):
            file.write("buzz\n") 
            continue
            
        elif (x % 3 == 0):
            file.write("fizz\n")
            continue
        
        file.write(f"{str(x)}\n")
        

    