num=19

while num>=10:
    dsum=0
    while num!=0:
        dsum+=(num%10)**2
        num//=10
    num=dsum
    
if dsum==1:
    print('happy number')
else:
    print('Not a happy number')
    
    