#!/usr/bin/python3.8
import dis

if __name__ == '__main__':
    with open('hidden_4.pyc', 'rb') as file:
        bytecode = file.read()

    code = dis.Bytecode.from_code(bytecode)
    names = [instr.argval for instr in code if instr.opname == 'LOAD_CONST']

    for name in sorted(names):
        if not name.startswith('__'):
            print(name)
