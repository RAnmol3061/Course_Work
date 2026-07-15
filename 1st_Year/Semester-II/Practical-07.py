def gcd(a, b) -> int:
    if b > a:
        a, b = b, a  # To make sure a is greater than b
    a, b = b, a % b
    return a


print(gcd(10, 100))
print(gcd(100, 100))
