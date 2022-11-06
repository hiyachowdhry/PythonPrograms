from fact import factorial
def series(x,n):
    assert n > 0, 'invalid number'
    e = 2
    s = 1
    sign = 1
    for i in range(n - 1):
        sign *= -1
        s += sign * (x ** e) / factorial(e)
        e += 2
    return s
x=int(input("Enter value of x: "))
n=int(input("Enter value of n: "))
print(series(x,n))
