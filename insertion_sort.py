def insertion_sort(x):
    """
    Funksioni që implementon algoritmin e Insertion Sort për të renditur një listë në mënyrë ngjitëse.
    """
    n = len(x)  # Gjejmë numrin e elementëve në listë
    for i in range(1, n):  # Fillojmë nga i dyti element (indeksi 1) deri tek i fundit
        aux = x[i]  # Ruajmë vlerën aktuale në një variabël ndihmëse
        j = i - 1  # Fillojmë krahasimin me elementin e fundit të pjesës së renditur

        # Zhvendosim elementët më të mëdhenj se 'aux' një pozicion djathtas
        while j >= 0 and aux < x[j]:
            x[j + 1] = x[j]
            j -= 1

        # Vendosim 'aux' në pozicionin e duhur
        x[j + 1] = aux

    return x  # Kthejmë listën e renditur


# Shembull përdorimi
if __name__ == "__main__":
    lista = [8, 4, 6, 2, 9]  # Lista që duam të rendisim
    print("Lista origjinale:", lista)
    lista_e_renditur = insertion_sort(lista)
    print("Lista e renditur:", lista_e_renditur)
