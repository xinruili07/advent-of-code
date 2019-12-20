
input1 = open("input1.txt", "r")

orbits = input1.read().split("\n")
orbits = [orbit.split(")") for orbit in orbits]

#part 1
list1 = []
for x in range(len(orbits)):
    for y in range(len(orbits[x])):
        list1.append(orbits[x][y])

planets = list(set(list1))
planets.remove("COM")

def findOrbits(orbitList, planet, count):
    for i in orbitList:
       
        localCount = count
        end = i[0]
        debut = i[1]
       
        if(debut == planet):
            if(end != "COM"):
                localCount += 1
                returnValue = findOrbits(orbitList, end,localCount)
            else:
                localCount +=1
                returnValue = localCount
               
    return returnValue

total = 0
for planet in planets:
    total += findOrbits(orbits, planet, 0)

print(total)