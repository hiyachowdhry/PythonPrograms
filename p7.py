def lenstr(s):
    c=0
    for i in s:
        c=c+1
    return c
def maxstr(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
def replacestr():
    a=input("Enter a string: ")
    for i in a:
        if i in "aeiouAEIOU":
            a=a.replace(i,'#')
    return a
def nwords():
    a=input("Enter a string: ")
    c=0
    for i in a:
        if i==' ':
            c+=1
    return c+1
def palinstr():
    x=input("Enter a string: ")
    w = ""
    for i in x:
        w = i + w
    if (x == w):
        print("It is Palindrome")
    else:
        print("It is not Palindrome")
def main():
    ans='y'
    while ans=='y':
        print('''
                      MENU
===================================================
(1) Find the length of string.
(2) Return maximum of three strings.
(3) Accept a string and replace all vowels with '#'
(4) Find number of words in the given string.
(5) Check whether the string is a palindrome or not.
(6) Exit
        ''')
        ch=int(input("Enter Choice: "))
        if ch==1:
            s=input("Enter a string: ")
            print("Length of the string is: ",lenstr(s))
        elif ch==2:
            a=input("Enter 1st string: ")
            b=input("Enter 2nd string: ")
            c=input("Enter 3rd string: ")
            print("The maximum of all three strings is: ",maxstr(a,b,c))
        elif ch==3:
            print(replacestr())
        elif ch==4:
            print(nwords())
        elif ch==5:
            print(palinstr())
        elif ch==6:
            break
        else:
            print("Wrong Choice.")
        ans=input("Do you wish to continue(y/n)?: ")

main()
        
        
