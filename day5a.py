import sys

file = open(sys.argv[1])
buffer = file.read()
mem = map(int, buffer.split(','))
end = len(mem)

pointer = 0

while(pointer < end):
    #Fetch
    opcode = mem[pointer] % 100

    if opcode == 99: #HALT
        break

    #Get modes
    m = mem[pointer] / 100
    modes = []
    for _ in range(3):
        modes.append(m % 10)
        m = m / 10

    #Set args
    args = mem[(pointer + 1):(pointer + 4)]
    for i in range(2):
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
        mem[mem[pointer + 1]] = input("Input requested:")
        pointer += 2

    elif opcode == 4: #Output
        print "Output: ", args[0]
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
