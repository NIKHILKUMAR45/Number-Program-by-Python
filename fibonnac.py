'write a program to print fibonnaci value of given position'


pos=int(input("Enter the number: "))

f,s=0,1
if pos>0:
    for _ in range(pos):
        print(f)
        f,s=s,f+s
        
    