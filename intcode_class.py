class intCode:

    def __init__(self, file1, phase, pointer):
        self.phase = phase
        self.pointer = pointer
        self.inputCount = 0
        input1 = open("input2.txt", "r")
        self.intcode = [int(element) for element in input1.read().split(",")]
        input1.close()
    
    def run(self, inputValue):
        original = self.intcode
        index = self.pointer

        def value(self, mode, position):
            value = 0
            if(mode == 0):
                value = original[original[position]]
            else:
                value = original[position]
            return value

        while original[index] != 99:
            intmodes = list(str(original[index]))
            while len(intmodes) < 5:
                intmodes.insert(0, "0")
            intmodes = [int(element) for element in intmodes]
            
            if intmodes[4] == 1:
                original[original[index+3]] = value(intmodes[2], index+1) + value(intmodes[1], index+2)
                index += 4

            elif intmodes[4] == 2:
                original[original[index+3]] = value(intmodes[2], index+1) * value(intmodes[1], index+2)
                index += 4
            
            #part 1
            elif intmodes[4] == 3:
                if (self.inputCount == 0):
                    inputval = self.phase
                    self.inputCount += 1
                else:
                    inputval = inputValue
                original[original[index+1]] = inputval
                index += 2

            elif intmodes[4] == 4:
                returnValue = value(intmodes[2], index+1)
                index += 2
                break
            
            #part 2
            elif intmodes[4] == 5:
                if value(intmodes[2], index+1) != 0:
                    index = value(intmodes[1], index+2)
                else:
                    index += 3

            elif intmodes[4] == 6:
                if value(intmodes[2], index+1) == 0:
                    index = value(intmodes[1], index+2)
                else:
                    index += 3
            
            elif intmodes[4] == 7:
                if value(intmodes[2], index+1) < value(intmodes[1], index+2):
                    original[original[index+3]] = 1
                else:
                    original[original[index+3]] = 0
                index += 4

            elif intmodes[4] == 8:
                if value(intmodes[2], index+1) == value(intmodes[1], index+2):
                    original[original[index+3]] = 1
                    
                else:
                    original[original[index+3]] = 0
                index += 4
        return returnValue
