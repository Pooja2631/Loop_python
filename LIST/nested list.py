# a=["a","b",["c",["d","e"],["j","g"],"k"],"l","m","n"]
# i=0
# b=[]
# while i<len(a):
# 	if type(a[i])==type([]):
# 		j=0
# 		while j<len(a[i]):
# 			if type(a[i][j])==type([]):
# 				k=0
# 				while k<len(a[i][j]):
# 					b.append(a[i][j][k])
# 					k+=1
# 			else:
# 				b.append(a[i][j])
# 			j+=1
# 	else:
# 		b.append(a[i])
# 	i+=1
# print(b)

# user=int(input("enter your number...."))
# li=[]
# i=1
# while i<(user):
#     user1=int(input("enter your number...."))
#     list=[]
#     j=0
#     while j<i:
#         list.append(user1)
#         j=j+1
#         break
#     i=i+1
#     li.append(list)
# print(li)  
# 
# 
# a=['a', 17, 12, 'a', 17, 18, 'b', 17, 14, 12, 19, 17, 'b',12, 13, 11]
# i=0
# b=[]
# while i<len(a):
# 	j=0
# 	c=[]
# 	count=0
# 	while j<len(a):
# 		if a[i]==a[j]:
# 			count=count+1
# 		j=j+1
# 	c.append(a[i])
# 	c.append(count)
# 	if c not in b:
# 		b.append(c)
# 	i=i+1
# print(b)

a=['red', 'white', 'a', 'b', 'black', 'f']
i=0
string= ""
while i<len(a):
    string=string+(a[i])
    # print(string)
    string.split(a[i])
    i=i+1
print(string)