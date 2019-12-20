
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
    for orbit in orbitList:
       
        localCount = count
        end = orbit[0]
        debut = orbit[1]
       
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

#part 2
def findPath(orbitList, planet, array):
    for orbit in orbitList:
       
        localArray = array
        end = orbit[0]
        debut = orbit[1]
       
        if(debut == planet):
            if(end != "COM"):
                localArray.append(orbit)
                returnArray = findPath(orbitList, end, localArray)
            else:
                localArray.append(orbit)
                returnArray = localArray
                break
    return returnArray

YOU_LIST = findPath(orbits, "YOU", [])
SANTA_LIST = findPath(orbits, "SAN", [])
count = 0 
for path1 in YOU_LIST:
    for path2 in SANTA_LIST:
        if path1[0] == path2[0] and path1 != path2:
            count = YOU_LIST.index(path1) + SANTA_LIST.index(path2)

print(count)