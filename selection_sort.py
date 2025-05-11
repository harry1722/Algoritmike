def selection_sort(x):
    """
    Funksioni selection_sort rendit një listë x në rend rritës duke përdorur algoritmin Selection Sort.
    """
    n = len(x)  # Gjejmë gjatësinë e listës
    # Për çdo element nga i pari deri te parafundit (n-1)
    for i in range(n - 1):
        k = i  # Kemi si supozim që elementi aktual është më i vogli
        # Krahasojmë elementin aktual me të tjerët në pjesën e parenditur të listës
        for j in range(i + 1, n):
            if x[k] > x[j]:  # Nëse gjejmë një element më të vogël
                k = j  # Ruajmë indeksin e elementit më të vogël
        # Nëse elementi më i vogël nuk është në pozicionin aktual
        if k != i:
            x[i], x[k] = x[k], x[i]  # Ndërrojmë vendet e elementit aktual me atë më të vogël
    return x  # Kthejmë listën e renditur

# Shembull përdorimi
x = [64, 25, 12, 22, 11]
print("Lista e parenditur: ",x)
print("Lista e renditur:", selection_sort(x))
