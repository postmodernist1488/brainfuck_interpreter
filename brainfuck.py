#this program can run brainfuck files

MEM_CAP = 3000

brainfuck_symbols = {'>', '<', '+', '-', '.', ',', '[', ']'}

def parse_code(code:str) -> str:
    return list(filter(lambda x: x in brainfuck_symbols, code))
    #could possibly ''.join() the filter object => need to choose between list and string

                                          # returns dict of the form:
def crossreference(program):              # {opening(closing) bracket position: corresponding closing(opening) position}
    left, blocks = [], {} 
    for i in range(len(program)):
        if program[i] == '[':
            left.append(i)
        elif program[i] == ']':
            blocks[left.pop()] = i

    blocks.update({value:key for key, value in blocks.items()})
    return blocks


def run_program(program:str):
    program = parse_code(program)
    arr = [0] * MEM_CAP
    pointer = 0
    i = 0
    loop = 0
    blocks = crossreference(program)
    while i < len(program):
        op = program[i]
        if op == '>':
            pointer += 1
        elif op == '<':
            pointer = max(0, pointer - 1)
        elif op == '+':
            arr[pointer] += 1
        elif op == '-':
            arr[pointer] -= 1
        elif op == '.':
            print(chr(arr[pointer]), sep='', end='')
        elif op == ',':
            arr[pointer] = int(input())
        elif op == '[':
            if not arr[pointer]:
                i = blocks[i]
        elif op == ']':
            if arr[pointer]:
                i = blocks[i]
        i += 1

with open('examples/hello_world.b', encoding='utf-8') as file:
    run_program(file.read())