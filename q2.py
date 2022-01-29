# a=1 
# while a<=10:
#     print(a)
#     a=a+1

# a=2
# while a<=12:
#     print(a)
#     a=a+2

# i=67
# while i<=78:
#     print(i)
#     i=i+2

user=int(input("enter your number"))
i=2
while i<=user:
    j=2
    co=0
    while j<i:
        if i%j==0:
            co=co+1
        j=j+1
    if co==0:
        print(i,"prime")      
    i=i+3 
  
# i=0
# while i<=3:
#     i=i+1
#     if i==2:
#         continue
#     print(i)
       
# i=25
# while i<=35:
#     print(i)
#     i=i+2