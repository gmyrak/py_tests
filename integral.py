def f(x):
    return (1 - x**2)**(1/2)
dx = 1e-6
x1, x2 = (0, 1)
x = x1
S = 0
while x < x2:
    S += f(x)*dx
    x += dx
print(4*S)

