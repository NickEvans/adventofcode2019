import sys
from itertools import permutations 

def run(inputStack, program):
    mem = program
    pointer = 0
    end = len(program)
    
    while(pointer < end):
        #Fetch
        opcode = mem[pointer] % 100

        if opcode == 99: #HALT
            break

        #Read modes
        m = mem[pointer] / 100
        modes = []
        for _ in range(3):
            modes.append(m % 10)
            m = m / 10

        #Read args
        args = mem[(pointer + 1):(pointer + 4)]

        #Input and output use fewer arguments
        if opcode == 3 or opcode == 4:
            argno = 1
        else:
            argno = 2

        #Change args to position/immediate modes
        for i in range(argno):
                if modes[i] == 0: #position mode
                    args[i] = mem[args[i]]

        #Execute
        if opcode == 1: #Add
            mem[args[2]] = args[0] + args[1]
            pointer += 4

        elif opcode == 2: #Mult
            mem[args[2]] = args[0] * args[1]
            pointer += 4

        elif opcode == 3: #Input
            mem[mem[pointer + 1]] = inputStack.pop()
            pointer += 2

        elif opcode == 4: #Output
            inputStack.append(args[0])
            pointer += 2

        elif opcode == 5: #Jump-if-true
            if args[0] != 0:
                pointer = args[1]
            else:
                pointer += 3
        
        elif opcode == 6: #Jump-if-false
            if args[0] == 0:
                pointer = args[1]
            else:
                pointer += 3
            
        elif opcode == 7: #Less than
            if args[0] < args[1]:
                mem[args[2]] = 1
            else:
                mem[args[2]] = 0
            pointer += 4

        elif opcode == 8: #Equals
            if args[0] == args[1]:
                mem[args[2]] = 1
            else:
                mem[args[2]] = 0
            pointer += 4

        else:
            print "Invalid opcode: ", opcode
            sys.exit("Exit failure")

    return inputStack

#Read input
file = open(sys.argv[1])
buffer = file.read()
program = map(int, buffer.split(','))

inputStack = [0]
phaseSettings = [0, 0, 0, 0, 0]
allSettings = list(permutations(range(5)))

largestOutput = 0

for p in allSettings:
    inputStack = [0]
    for i in range(5):
        inputStack.append(p[i])
        inputStack = run(inputStack, program)
    largestOutput = max(largestOutput, inputStack[0])

print(largestOutput)