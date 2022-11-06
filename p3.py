def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
l1=[]
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        num=Fibonacci(n-1)+Fibonacci(n-2)
        ans=factorial(num);
        l1=[num,ans]
        return l1
Fibonacci(12)
