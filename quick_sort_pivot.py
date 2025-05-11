def partition(arr, le, ri):
    #Choose the last element as the pivot
    pivot = arr[ri]
    i = le - 1 #Index for the smaller element
    
    for j in range (le, ri):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] #Swap elements
            
    #Place the pivot in the correct position
    arr[i + 1], arr[ri], arr[i + 1]
    return i+1 #Return the pivot index
    
def quicksort1(arr, le, ri):
    if le < ri:
        #Partition the array and get the pivot index
        q = partition(arr, le, ri)
            
        #Recursovely sprt elements before and after the pivot
        quicksort1(arr, le, q - 1)
        quicksort1(arr, q + 1, ri)
            
        return arr
            
#Example usage
array = [10, 7, 8, 9, 1, 5]
sorted_array = quicksort1(array, 0, len(array)-1)
print("Sorted array: ", sorted_array)
