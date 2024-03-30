def prime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2

num=2
count=5
while count!=0:
    if prime(num):
        print(num)
        num+=1
        count-=1
    else:
        num+=1
