def bubble_sort(x):
    """
    Funksioni për renditjen e një liste x duke përdorur algoritmin Bubble Sort
    bazuar në pseudokodin e dhënë.
    """
    n = len(x)  # Gjatësia e listës
    # Cikli i jashtëm fillon nga fundi i listës deri te elementi i dytë
    for i in range(n, 1, -1):  # i zvogëlohet nga n deri në 2
        # Cikli i brendshëm krahaso elementët fqinj deri te i-1
        for j in range(1, i):  # j shkon nga 1 deri në i-1
            if x[j - 1] > x[j]:  # Nëse elementi aktual është më i madh se fqiu
                # Ndërro vendet e x[j-1] dhe x[j]
                x[j - 1], x[j] = x[j], x[j - 1]
    return x  # Kthe listën e renditur

# Shembull përdorimi
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista e parenditur: ", lista)
print("Lista e renditur:", bubble_sort(lista))
