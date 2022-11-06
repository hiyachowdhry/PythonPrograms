def digits():
    l1=[]
    n=int(input("Enter a number greater than 10: "))
    while(n>0):
        s=n%10
        n=n//10
        l1.append(s)
    print(set(l1))
digits()
