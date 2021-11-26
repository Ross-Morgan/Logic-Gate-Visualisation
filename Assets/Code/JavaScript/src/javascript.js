let orGate = (a, b) => a | b;
let andGate = (a, b) => a & b;
let norGate = (a, b) => 1 - (a | b);
let nandGate = (a, b) => 1 - (a & b);
let xorGate = (a, b) => a ^ b;
let xnorGate = (a, b) => 1 - (a ^ b);


function orGate(a, b) {
    return a | b;
}

function andGate(a, b) {
    return a & b;
}

function norGate(a, b) {
    return 1 - (a | b);
}

function nandGate(a, b) {
    return 1 - (a & b);
}

function xor(a, b) {
    return a ^ b;
}

function xnor(a, b) {
    return 1 - (a ^ b);
}