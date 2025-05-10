deg gcf(a,b):
  while b!=0:
    temp = b
    b = a %  b
    a = temp
  return a
numer1 = 48
numer2 = 12
result = gcf(numer1,numer2)
print("PMP e numrave 48 dhe 12 eshte: ", result)
