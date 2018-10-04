def sum(*args):
    s=0
    for x in args:
        s+= x
    return s

#print( sum(6,6,8))

hs = {}
hs['a'] = 'vsl'
hs['b']= 1

for k in hs.keys():
    print('{} => {}'.format(k, hs[k]))


#def factor(n):
