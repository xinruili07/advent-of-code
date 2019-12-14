#Day 4
import itertools

inputs = "145852-616942".split("-")
start = int(inputs[0])
end = int(inputs[1])

correct = 0

for password in range(start, end + 1):
    double = False
    increasing = True
    password = str(password)
    consecutives = [list(g) for k, g in itertools.groupby(password)]
    for group in consecutives:
        if len(group) == 2:
            double = True

    for index in range(len(password)-1):
        if (password[index] > password[index+1]):
            increasing = False
            break
    if (increasing and double):
        correct += 1
print(correct)

