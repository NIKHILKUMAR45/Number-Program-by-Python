def fib(pos):
    if pos==1 or pos==2:
        return pos-1
    
    return fib(pos-1) + fib(pos-2)

def first_5(num):
    if num==0:
        return num
    return fib(num-1)

num=5
print(first_5(num))
      
      
      wrong  apporach