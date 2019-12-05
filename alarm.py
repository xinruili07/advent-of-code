#day2

import sys
import random

required = 19690720
x = random.randint(0, 99)
y = random.randint(0, 99)
firstint = 0
original = [int(element) for element in sys.stdin.readline().strip().split(",")]

while firstint != required:
    line = original.copy()
    line[1] = x
    line[2] = y
    for index in range(0, len(line), 4):
        if line[index] == 99:
            break
        if line[index] == 1:
            line[line[index+3]] = line[line[index+1]] + line[line[index+2]]
        if line[index] == 2:
            line[line[index+3]] = line[line[index+1]] * line[line[index+2]]
    firstint = line[0]
    x = random.randint(0, 99)
    y = random.randint(0, 99)

print(firstint)
print("Answer: {} {}".format(line[1], line[2]))
    
    