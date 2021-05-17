def gcd(a, b):
    if a < b:
        return gcd(b, a)
    while a % b != 0:
        temp = b
        b = a % b
        a = temp
    return b

def test(a, b, c):
    d = (a-1) * (b-1)
    if gcd(d, c) == 1:
        # 互质
        return 1
    else:
        # 不互质
        return 0