package main

func orGate(a int, b int) int {
	return a | b
}

func andGate(a int, b int) int {
	return a & b
}

func norGate(a int, b int) int {
	return 1 - (a | b)
}

func nandGate(a int, b int) int {
	return 1 - (a & b)
}

func xorGate(a int, b int) int {
	return a ^ b
}

func xnorGate(a int, b int) int {
	return 1 - (a ^ b)
}