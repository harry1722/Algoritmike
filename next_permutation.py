# Funksioni për të identifikuar indeksin i parë nga fundi ku një element është më i vogël se elementi pas tij.
def identify(x):
    n = len(x)  # Gjej gjatësinë e listës.
    i = n - 1   # Fillon nga fundi i listës.
    # Gjej indeksin më të vogël ku elementi para tij është më i madh se elementi aktual.
    while (i > 0) and (x[i-1] > x[i]):
        i -= 1
    return i  # Kthen indeksin ku ndryshimi duhet të fillojë.

# Funksioni për të gjetur elementin më të vogël në intervalin [i+1, n) që është më i madh se x[i-1].
def minimum(x, i):
    n = len(x)  # Gjatësia e listës.
    k = i       # Fillon kërkimin nga indeksi i.
    # Iteron mbi listën për të gjetur elementin më të vogël më të madh se x[i-1].
    for j in range(i+1, n):
        if (x[j] < x[k]) and (x[j] > x[i-1]):
            k = j
    return k  # Kthen indeksin e elementit të zgjedhur.

# Funksioni për të ndërruar dy vlera.
def swap(a, b):
    return b, a  # Kthen vlerat e ndërruara.

# Funksioni për të përmbysur listën mes indekseve të dhëna.
def reverse(x, left, right):
    i = left      # Indeksi i majtë.
    j = right     # Indeksi i djathtë.
    # Përmbys elementet mes indekseve left dhe right.
    while i < j:
        x[i], x[j] = x[j], x[i]
        i += 1
        j -= 1
    return x  # Kthen listën e përditësuar.

# Lista fillestare.
x = [6, 3, 0, 9, 4, 8, 7, 5, 2, 1]
print("Digits of the initial number:", x)

# Gjej indeksin ku fillon ndryshimi për permutimin e ardhshëm.
i = identify(x)
print("i =", i)

# Gjej elementin më të vogël më të madh se x[i-1].
k = minimum(x, i)
print("k =", k)

# Ndërro vlerat mes x[i-1] dhe x[k].
x[i-1], x[k] = swap(x[i-1], x[k])
print("Sequence after swap:", x)

# Përmbys pjesën e listës nga indeksi i në fund.
x = reverse(x, i, len(x) - 1)
print("Sequence after reverse:", x)
