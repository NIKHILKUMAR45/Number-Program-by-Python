num=100
for dem in [2,3,5]:
    while num%dem==0:
        num//=dem
if num==1:
    print('ugly ')
else:
    print('not a ugly number')