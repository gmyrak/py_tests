import num

for k in range(2, 2000):
    if num.ferma(k) and not num.prime(k):
        print('{} = {}'.format(k, num.factor(k)))