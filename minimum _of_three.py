def min_of_three(a, b, c):
    if a < b: #a eshte a me e vogel se b
        if a < c: #nese eshte krahsojme a me c 
            m = a #nese a < c minimumi eshte a
        else:
            m = c #ndryshe eshte c
    else: #nese a eshte eshte me e madhe i ndodh qe b eshte me vogel se a
        if b < c:  #bejme krhasimin me c
            m = b #nese b eshte eshte me e vogel barazojme me m
        else:
            m = c# nese eshte c me e vogel ai eshte minimumi
    return m

# Shembull përdorimi:
print(min_of_three(3.5, 7.2, 1.8))  # Output: 1.8
