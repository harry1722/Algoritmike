def merge_with_sentinel(a, b):
    #Append "infinity" to both arrays
    a.append(float('inf'))
    b.append(float('inf'))
    
    c = []
    i = 0
    j = 0
    
    #Loop through the total length of the merged array
    for _ in range(len(a) + len(b) - 2):
        if a[i] <=b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            
    return c
    
#Example usage
a = [1, 3, 5]
b = [2, 4, 6]
print("Merged array: ", merge_with_sentinel(a, b))
        
