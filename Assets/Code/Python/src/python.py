def or_gate(a:int, b:int):
    return a | b

def and_gate(a:int, b:int):
    return a & b

def nor_gate(a:int, b:int):
    return 1 - (a | b)

def nand_gate(a:int, b:int):
    return 1 - (a | b)

def xor_gate(a:int, b:int):
    return a ^ b

def xnor_gate(a:int, b:int):
    return 1 - (a ^ b)
