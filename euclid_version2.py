def gcd(a, b):
    dd = a
    dr = b
    r = dd % dr
    while r != 0:
        dd = dr
        dr = r
        r = dd % dr
    return dr

# Shembull përdorimi
a = int(input("Shkruaj numrin e parë: "))
b = int(input("Shkruaj numrin e dytë: "))
print(f"GCD({a}, {b}) është: {gcd(a, b)}")
