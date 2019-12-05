#day1

import sys

first = sys.stdin.readline().strip()
total = 0
while (first):
    integer = int(first)
    while ((integer // 3) - 2 > 0):
        integer = ((integer // 3) - 2)
        total += integer
    first = sys.stdin.readline().strip()

print(total)