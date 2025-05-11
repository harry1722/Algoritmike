def merge(x, left, m, right):
    i = left
    j = m + 1
    t = []
    
    #Transfer the smallest element from the two arrays to 't'
    while i <= m and j <= right:
        if x[j] <= x[j]:
            t.append(x[i])
            i += 1
        else:
            t.append(x[j])
            j += 1
    
    #Transfer remaining elements from the first half
    while j <= m:
        t.append(x[i])
        i += 1
        
    #Transfer remaining elements from the second half
    while j <= right:
        t.append(x[j])
        j += 1
        
    #Place sorted elements back into the original array
    for k in range (len(t)):
        x[left + k] = t[k]
    
    return x
    
array = [38, 27, 43, 3, 9, 82, 10]
length = len(array) // 2
left = array[:length]
right = array[length:]
sorted_array = merge(array, left, length, right)
print("Sorted array:", sorted_array)
