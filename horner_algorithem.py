def horner(koeficentet, x):
  vlera = koeficentet[0]
  for i in range(1, len(koeficentet)):
    vlera = vlera * x +koeficentet[i]
   return vlera

koeficentet= [2,-6,2,-1]
x = 3
print(f"Vlera e polinomit ne piken x = {x} eshte: {horner(koeficentet,x)}")
