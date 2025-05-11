def merge_sort(arr):
    if len(arr) > 1:
        # Përça: Gjej pikën e mesit dhe ndaj listën në dy gjysma
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Sundo: Thirr rekursivisht merge_sort për secilën gjysmë
        merge_sort(left_half)
        merge_sort(right_half)

        # Kombino: Bashko dy gjysmat e renditura
        i = j = k = 0  # Indekset për left_half, right_half, dhe arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Shto elementet e mbetura nga left_half, nëse ka
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Shto elementet e mbetura nga right_half, nëse ka
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Shembull përdorimi
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Lista fillestare:", arr)
    merge_sort(arr)
    print("Lista e renditur:", arr)
