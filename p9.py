def main():
    d=dict()
    for i in range(4):
        name=input("Enter name of student: ")
        marks=int(input("Enter marks(max=100): "))
        d[name]=marks
    print("Student scoring highest is: ")
    highestperc(d)
def highestperc(d):
    print(max(d,key=d.get))
main()
