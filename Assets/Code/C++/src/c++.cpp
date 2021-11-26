int orGate(int a, int b) {
    return a | b;
}

int andGate(int a, int b) {
    return a & b;
}

int norGate(int a, int b) {
    return 1 - (a | b);
}

int nandGate(int a, int b) {
    return 1 - (a & b);
}

int xorGate(int a, int b) {
    return a ^ b;
}

int xnorGate(int a, int b) {
    return 1 - (a ^ b);
}