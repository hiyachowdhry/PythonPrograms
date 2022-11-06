def eleno(L):
    for i in L:
        if i.isnumeric():
            return True
        else:
            return False
def elestr(L):
    for i in L:
        if type(i)==str:
            return True
        else:
            return False
def revlist(L):
    return L[::-1]
def findele(L,e):
    for i in range(0, len(L), 1):
        if L[i] == e:
            return True
    return False
def removele(L,e):
    if (findele(L, e)):
        L.remove(e)
        return True
    return False
def desclist(L):
    L.sort(reverse=True)
    return L
def commonele(L1,L2):
    for i in L1:
        if i in L2:
            print(i,end=' ')

def main():
    l=[]
    l2=[]
    c=0
    n=int(input("Enter number of elements: "))
    for i in range(n):
        a=input("Enter elements: ")
        l.append(a)
    if(eleno(l)):
        print("Given list is numeric list.")
        for i in l:
            if not int(i)%2==0:
                c+=1
        print("Number of odd elements in list are: ",c)
    elif(elestr(l)):
        print("Given list is string list.")
        print("Max string is ",max(l))
    print("list in reverse order is: ",revlist(l))
    e = input('Enter Search Element: ')
    if (findele(l, e)):
        print('Element Found in List')
    else:
        print('Element Not Found in List')

    e = input('Enter Element to Remove: ')
    r = removele(l,e)
    if (r):
        print('List after Removing Element:', l)
    else:
        print('Element Not Found in List')
    print("List in descending order: ",desclist(l))
    print()
    n2=int(input("Enter elements in list 2: "))
    for i in range(n2):
        b=input("Enter elements: ")
        l2.append(b)
    commonele(l,l2)
main()
        
