class Main {
    static int orGate(int a, int b) {
        return a | b;
    }

    static int andGate(int a, int b) {
        return a & b;
    }

    static int norGate(int a, int b) {
        return 1 - (a | b);
    }

    static int nandGate(int a, int b) {
        return 1 - (a & b);
    }

    static int xorGate(int a, int b) {
        return a ^ b;
    }

    static int xnorGate(int a, int b) {
        return 1 - (a ^ b);
    }
}