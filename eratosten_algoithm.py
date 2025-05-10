def prim_numbers(n):
    # Krijojmë një listë të quajtur 'prim' që përfaqëson nëse një numër është prim.
    # Fillimisht, të gjithë numrat janë supozuar si prim (True).
    prim = [True] * (n + 1)
    # Shënojmë 0 dhe 1 si jo-prime (False), pasi ato nuk janë numra prim.
    prim[0] = prim[1] = False

    # Fillojmë kontrollin për numrat nga 2 deri në n.
    for i in range(2, n + 1):
        # Kontrollojmë nëse numri aktual 'i' është ende prim.
        if prim[i]:
            # Nëse 'i' është prim, shënojmë të gjithë shumëfishat e tij si jo-prime (False).
            for j in range(2 * i, n + 1, i):
                prim[j] = False

    # Krijojmë një listë të numrave prim duke mbledhur të gjithë indeksat 'i' ku 'prim[i]' është True.
    prim_numbers = [i for i in range(n + 1) if prim[i]]
    # Kthejmë listën e numrave prim.
    return prim_numbers

# Shembull përdorimi:
# Printojmë numrat prim deri në 20. Rezultati do të jetë: [2, 3, 5, 7, 11, 13, 17, 19]
print(prim_numbers(20))
