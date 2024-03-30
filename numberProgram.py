# Prime Number
def prime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2

# Compositive number
def compositive(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount>2

 # Perfect number
def perfect(num,dsum=0):
    for fa in range(1,num):
        if num%fa==0:
            dsum+=fa
    return dsum==num

# Pronic number
def pronic(num,n=0):
    while n*(n+1)<=num:
        if n*(n+1)==num:
            return True
        n=n+1
    return False

# Sunny number
def sunny(num,n=1):
    while n**2<=(num+1):
        if n**2==num+1:
            return True
        n+=1
    return False

# Niven number
def niven(num,dsum=0):
    copy=num
    while num!=0:
            rem = num%10
            dsum += rem
            n = n//10
    return dsum==copy

# Spy number
def spy(num,dsum=0,dprod=1):
    while num!=0:
        rem = num%10
        dsum+=rem
        dprod *=rem
        num //=10
    return dsum==dprod

# Niven number
def niven(num,dsum=0):
    sq=num**2
    while sq!=0:
        rem=num%10
        dsum+=rem
        sq //=10
        
    return num==dsum

# Reverse number
def reverse(num,rev=0):
    while num!=0:
        rem= num%10
        rev=rev*10+rem
        num //= 10
        
    return  rev

# Palindrome number
def palindrome(num):
    
    return num == reverse(num)

# Armstrong number
def armstrong(num,dsum=0):
    p=len(str(num)) 
    copy=num
    while num!=0:
        rem=num%10
        dsum = dsum + rem**p
        num //= 10
    return copy== dsum  



# Dsiarium number
def disarium(num,dsum=0):
    p=len(str(num))
    copy=num
    while num!=0:
        rem=num%10
        dsum+=rem**p
        num//=10
        p-=1
    return copy==dsum;

# Palyprime number
def palyprime(num):
    return (num==reverse(num)) and prime(num)


# Emrip number
def emrip(num):
    return (num!=reverse(num)) and prime(num) and prime(reverse(num))

# Factorial number
def factorial(num,fact=1):
    for fa in range(1,num+1):
        fact*=fa
    return fact


# Strong number
def strong(num,dsum=0):
    copy=num
    while num !=0:
        rem=num%10
        dsum=dsum+factorial(rem)
        num=num//10
    return copy==dsum

# Evil or Odious Number
def evilorOdious(num,count=0):
    while num!=0:
        rem=num%2
        if rem==1:
            count += rem
        num //= 2
    if (count%2==0):
        return 'Evil Number'
    else:
        return 'Odious Number'


# Automorfic number
def automorfic(num):
    p=len(str(num))
    sq=num**2
    return num==sq%(10**p)

# Trimorfic number
def trimorfic(num):
    p=len(str(num))
    cube=num**3
    return num == cube%(10**p)


def digsum(num,dsum=0):
    while num!=0:
        rem=num%10
        dsum+= rem**2
        num //= 10
    return dsum

# Happy number
def happy(num):
    while num>=10:
          num=digsum(num)
    return num==1

# Tech number
def tech(num,dsum=0):
    h=len(str(num))
    if h%2!=0:
        return 'Not possible'
    else:
        p=h//2
        fh=num%(10**p)
        sh=num//(10**p)
    return (fh+sh)**2 ==num


    
    
        
        