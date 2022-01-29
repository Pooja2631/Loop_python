
list=[3,4,8,2,45,6,12,43,35,2] 
i=0
while i<len(list)-1:
    if i%3==0:
        print(list[i],"prime number") 
    else:
        print(list[i]," not prime number")
    i=i+1
          