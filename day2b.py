import sys

solution = 19690720 #Desired output

file = open(sys.argv[1])
buffer = file.read()
program = map(int, buffer.split(','))
end = len(program)

for noun in range(100):
    for verb in range(100):

        pointer = 0
        mem = map(int, buffer.split(','))
        mem[1] = noun
        mem[2] = verb

        while(pointer < end):
            opcode, arg1, arg2, add = mem[pointer:(pointer + 4)]
            if opcode == 1: #Add
                mem[add] = mem[arg1] + mem[arg2]
                pointer += 4
            elif opcode == 2: #Mult
                mem[add] = mem[arg1] * mem[arg2]
                pointer += 4
            elif opcode == 99: #Halt
                break
            else:
                print(opcode)
                sys.exit("Invalid opcode")

        if mem[0] == solution:
            print(noun)
            print(verb)
            sys.exit()