import Data.Bits(Bits, (.|.), (.&.))

xor = (/=)

orGate a b =  (.|.) a b
andGate a b =  (.&.) a b
norGate a b =  1 - ((.|.) a b)
nandGate a b =  1 - ((.&.) a b)
xorGate a b =  xor a b
xnorGate a b =  1 - (xor a b)