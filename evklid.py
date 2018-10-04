def NOD(a, b):
    while(a>0):
        a,b = b%a,a
    return b

def NOK(a, b):
    return (a*b)//NOD(a,b)

# print(NOD(135, 60))
#
#
# for i in range(10):
#     print(i)

a = 7
b = 12

#a, b = b, a

print(2**3000)

