def prime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2


def reverse(num,rev=0):
    
    while num!=0:
        rev=rev*10+num%10
        num //= 10
    return rev


def palyprime(num):
    if reverse(num)==num and prime(num):
        print('palyprime')
    else:
        print('not a palyprime number')
    
def emrip(num):
    if reverse(num) != num and prime(num) and prime(reverse(num)):
        print('emrip number')
    else:
        print("not emrip number")

emrip(17)
palyprime(71)