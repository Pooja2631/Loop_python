# i=1
# while i<=6:
#     b=1
#     while b<=1:
#         print(i,end=" ")
#         b+=1
#     print()
#     i+=1

i=1
while i<=5:
    j=1
    while j<=i:
        if i%2==0:
            print("*",end=" ")
        else:
            print(j,end=" ")
        j+=1
    print( )
    i+=1