import sys

file = open(sys.argv[1])
buffer = file.read()
mem = map(int, buffer.split(','))
end = len(mem)

pointer = 0

while(pointer < end):
    opcode = mem[pointer] % 100 #DE
    #modes = [int(d) for d in str(mem[pointer] / 100).zfill(3)] #A, B, C
    m = mem[pointer] / 100
    modes = []
    for i in range(3):
        modes.append(m % 10)
        m = m / 10
    args = mem[(pointer + 1):(pointer + 4)]

    if opcode == 1: #Add
        for i in range(2):
            if modes[i] == 0: #position mode
                args[i] = mem[args[i]]
        mem[args[2]] = args[0] + args[1]
        pointer += 4

    elif opcode == 2: #Mult
        for i in range(2):
            if modes[i] == 0: #position mode
                args[i] = mem[args[i]]
        mem[args[2]] = args[0] * args[1]
        pointer += 4

    elif opcode == 3: #Input
        mem[args[0]] = input("Input requested:")
        pointer += 2

    elif opcode == 4: #Output
        if modes[0] == 0:
            print "Output: ", mem[args[0]]
        else:
            print "Output: ", args[0]
        pointer += 2

    elif opcode == 5: #Jump-if-true
        for i in range(2):
            if modes[i] == 0: #position mode
                args[i] = mem[args[i]]
        if args[0] != 0:
            pointer = args[1]
        else:
            pointer += 3
    
    elif opcode == 6: #Jump-if-false
        for i in range(2):
            if modes[i] == 0: #position mode
                args[i] = mem[args[i]]
        if args[0] == 0:
            pointer = args[1]
        else:
            pointer += 3
        
    elif opcode == 7: #Less than
        for i in range(2):
            if modes[i] == 0: #position mode
                args[i] = mem[args[i]]
        if args[0] < args[1]:
            mem[args[2]] = 1
        else:
            mem[args[2]] = 0
        pointer += 4

    elif opcode == 8: #Equals
        for i in range(2):
            if modes[i] == 0: #position mode
                args[i] = mem[args[i]]
        if args[0] == args[1]:
            mem[args[2]] = 1
        else:
            mem[args[2]] = 0
        pointer += 4

    elif opcode == 99: #Halt
        #print("HALT. Final state:")
        #print(mem)
        break

    else:
        print(opcode)
        sys.exit("Invalid opcode")
