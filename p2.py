def sales():
    n=int(input("Enter the number of salesmen: "))
    tot=0
    l1=[]
    l2=[]
    for i in range(1,n+1):
        print("Salesman ",i)
        for j in range(1,5):
            sales=int(input("Enter sales done by salesman in week %d: " %j))
            tot=tot+sales
        l1.append(tot)
        if tot<50000:
                commission=0
        else:
                commission=0.05*tot
        #totalsales=sales+commission
    
        l1.append(commission)
        if(tot>=80000):
            l1.append("Excellent")
        elif(tot>=60000 and tot<80000):
            l1.append("Good")
        elif(tot>=40000 and tot<60000):
            l1.append("Average")
        else:
            l1.append("Work Hard")
    return l1
print(sales())
        
        
