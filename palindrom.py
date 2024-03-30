def palindrome(num,rev=0):
    copy=num
    while num!=0:
        rev=rev*10+num%10
        num=num//10
    return rev == copy

print(palindrome(122))
        
        
        
        
    