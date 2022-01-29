number=[1,0,0,1,1,0,1,1]
i=len(number)-1
c=1
decimal =0
while i>=0:
       decimal=decimal+number[i]/c
       c=c/2
       i=i+1

a=[2,3,4,5,6,8]
b=[54,12,78,9]
c=[]
i=0
sum=0
while i<len(a):
     sum=b[i]+a[i]
     c.append(sum)
     i=i+1
print(c)
