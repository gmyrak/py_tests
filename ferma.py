def expmod(x, n, m):
    res=1
    x%= m
    while(n>0):
        if n%2==0:
            n//=2
            x= x*x % m
        else:
            res= res*x %m
            n-=1
    return res


def pseudo(n):
    # for i in [3, 5, 7, 11]:
    #     if n%i == 0: return False
    for k in [2]:
        if expmod(k, n, n) !=k: return False
    return True

def simple(n):
    i = 2
    while i*i<=n:
        if n % i == 0:
            return False
        i+=1
    return True

for k in range(2, 10000):
    if pseudo(k) and not simple(k):
        print(k)

#print(expmod(2, 7))