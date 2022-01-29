# a=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     c=[]
#     count=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count=count+1
#         j=j+1
#     c.append(a[i])
#     c.append(count) 
#     if c not in b:
#             b.append(c)  
#     i=i+1
# print(b) 


# a=["a","m","r","i","t","a"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     c=[]
#     count=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count=count+1
#         j=j+1
#     c.append(a[i])
#     c.append(count)
#     if c not in b:
#             b.append(c)
#     i=i+1
# print(b)            


a=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
b=[]
while i<len(a):
    j=0
    c=[]
    while j<len(a):
        if a[i]==a[j]:
            j=j+1
    c.append(a[i])
    if c not in b:
        b.append(c)
i=i+1
print(b)




