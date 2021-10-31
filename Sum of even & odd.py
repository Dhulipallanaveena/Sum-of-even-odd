n=int(input())
sum1=0
sum2=0
m=n
while m>0:
    rem=m%10
    if rem%2==0:
        sum1=sum1+rem
    else:
        sum2=sum2+rem
    m=m//10
print(sum1,sum2)
