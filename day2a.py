import sys

filepath = sys.argv[1]

file = open(filepath)
buffer = file.read()
program = map(int, buffer.split(','))
end = len(program)

#Restore 1202 Alert
program[1] = 12
program[2] = 2

def addOp(i):
    program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]

def multOp(i):
    program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]

def execute(op, pos):
    opList = {
        1: addOp,
        2: multOp
    }
    opList.get(op, lambda x: 'Invalid opCode')(pos)

p = 0
while(p < end):
    opcode = program[p]
    if opcode == 99: #Halt
        break
    execute(opcode, p)
    p += 4

print(program[0]) #Solution