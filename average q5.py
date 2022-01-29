     
a=[23,14,56,12,19,9,15,25,31,42]
i=0
sum=0
sum1=0
count1=0
count2=0

while i<len(a):
    if a[i]%2==0:
        print("even number",a[i])
        count=count1+1
        sum=sum1+a[i]
        average=sum//count1
    else:
        print("odd number",a[i]) 
        count2=count2+1
        sum1=sum1+a[i] 
        average1=sum1//count2
    i=i+1
    print(count1,"even",sum,average)
    print(count2,"odd",sum1,average)  

