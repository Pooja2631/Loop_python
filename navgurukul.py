# i=1
# while i<=100:
#     if i%3==0:
#         print("nav")
#     elif i%7==0:
#         print("gurukul") 
#     else:
#         print(i)
#     i+=1      


user=int(input("enter your number"))
i=1
while i<=100:
    if i%3==0 and i%7==0:
        print(i,"navgurukul")
    elif i%3==0:
        print(i,"nav") 
    elif i%7==0:
        print(i,"gurukul") 
    else:
        print(i)   
    i+=1           
        
        
