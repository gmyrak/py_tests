def nod(a, b):
    while a > 0:
        a, b = b%a, a
    return b


def nok(a, b):
    return a*b//nod(a, b)


def sqr(n):
     x1 = n
     while True:
        x2 = (x1 + n//x1)//2
        if x1 > x2:
            x1 = x2
        else:
            return x1


def expm(x, n, m):
    x %= m
    res = 1
    while n > 0:
        if n % 2 == 0:
            x = x*x % m
            n //= 2
        else:
            res = res*x % m
            n -= 1
    return res


def ferma(n):
    return expm(2, n, n) == 2


def prime(n):
    i = 3
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        sq = sqr(n)
        while i <= sq:
            if n % i == 0:
                return False
            i += 2
        return True


def factor(n):
    pr = []
    k = 2
    while k <= sqr(n):
        while n % k == 0:
            n //= k
            pr.append(k)
        k += 1
    if n > 1:
        pr.append(n)
    return pr

