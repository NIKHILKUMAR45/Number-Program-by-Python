def nextprime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2

num=2
num+=1
while not nextprime(num):
    num+=1
print(num)