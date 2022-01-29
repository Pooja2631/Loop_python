# list=[10,20,12,22]
# i=0
# sum=0
# while i<len(list):
#     sum=sum+list[i]
#     i=i+1
# print(sum) 

# list=[3,4,-9,4]
# i=0
# sum=0
# while i<len(list):
#     sum=sum+list[i]
#     i=i+1
# print(sum)    

# list=[-3,-23,-9,-12]
# i=0
# sum=0
# while i<len(list):
#     sum=sum+list[i]
#     i=i+1
# print(sum)    


# list=[3,1,2,3]
# i=0
# mul=1
# while i<len(list):
#     mul=mul*list[i]
#     i=i+1
# print(mul)  

# list=[8,-5,22,-3]
# i=0
# max=0
# while i<len(list):
#     max=max+list[i]
#     i=i+1
# print(max)    
 
# num = [8,-3,22,12]
# index=0
# min=num[0]
# while index<len(num):
#     if num[index] <min:
#         min=num [index]
#     index=index+1
# print(min)
         

# list=['abc','aba','xyz','1221','mom']
# i=0
# co=0 
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         # j=j+1
#         if list[i]==list[-j]:
#             co=co+1
#             print(co)
#         else: 
#             j=j+1
#         i=i+1     
            
# list=[10,20,30,20,10,40,50,60]
# c=[]
# i=0
# while i<len(list):
#     if list[i] not in c:
#         c.append(list[i])
#     i=i+1  
# print(c)


# a=(input("enter something:"))
# i=-1
# while i>=-len(a):
#     print(a[i])
#     i-=1
 

# list=["1","2","3","4","5","6"]
# i=0
# a=[]
# while i<len(list):
#     c=list[i]+list[i+1]
#     a.append(c)
#     i=i+2
# print(a)  


# from random import shuffle
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)

# list1=["n","i","t","i","n"]
# rev=0
# i=0
# while i>-(len(list1)):
#     print(list1[-i])
#     i=i-1


# user=int(input("enter your number:-"))
# i=0
# while i<=user:
#     if user%2==0:
#         print("user")
#     a=user//2    

# list=[11,33,50]
# string="" 
# i=0
# while i<len(list):
#     string = string + str(list[i])
#     i=i+1
# print(string)

# list1=["a","m","r","i","t","a"]
# i=-1
# li=[]
# while i>=-(len(list1)):
#     li.append(list1[i])
#     i=i-1
# print(li)

# list=[2,4,6,8,11,13]
# i=0
# b=[]
# while i<len(list)-1:
#     c=[]
#     c.append(list[i])
#     c.append(list[i+1])
#     b.append(c)
#     i=i+2
# print(b)

# my_list = ['p', 'q']
# n = 4
# new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
# print(new_list)

# my_list=['p','q']
# n=int(input("enter the number.........."))
# i=1
# b=[]
# co=0
# while i<len (my_list):
#     b.append(my_list)
#     co=co+1
#     i=i+1
# print(b,co)

# a=[2,3,4,5,6,7,8,9,12]
# index=0
# while index<len(a):
#     if index %2==0:
#         print(index," even number")
#     else:
#         print(index,"  odd number") 
#     index+=1 

# a=[[1,2,3],[2,3,4],[1,2,3],[12,[23]]]
# print(len(a))

# a=[1,2,3,4,5,6,7,8,9]
# print(len(a))

# list=["2","3","4","5"]
# i=0
# a=[]
# while i<len(list):
#     c=list[i]+list[i+1]
#     a.append(c)
#     i=i+2
# print(a)


# list=['2','3','4','5']
# i=0
# sum=0
# while i<len(list):
#     sum=sum+int(list[i])
#     i=i+1
# print(sum)

# a=['2','a',4,5.6]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+int(a[i])
#     i=i+1
# print(sum)

# list=[1, 2, 2, 5, 8, 4, 4, 8]
# c=[]
# i=0
# while i<len(list):
#     if list[i] not in c:
#         c.append(list[i])
#     i=i+1  
# print(c)

# a=[[1,2,3],[1,2,4,6]]
# i=0
# sum=0
# sum1=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         sum=sum+(a[i][j])
#         sum1=sum1+(a[i][j])
#         j=j+1
#     i=i+1
# print(sum)

# a=[1234,1294,122,1984,100]
# i=0
# compare=str (a[0])
# compare=compare[0]
# while i<len(a):
#     element=str(a[i])
#     if element[0]!=compare:
#         Ans=False
#         break
#     ans=True
#     i=i+1
# print(ans)    


# list=[[10, 20], [40], [30, 50, 60], [10, 20], [33], [40]]
# c=[]
# i=0
# while i<len(list):
#     if list[i] not in c:
#         c.append(list[i])
#     i=i+1  
# print(c)

# list=[9,1,1,9]
# i=0
# while i<len(list):
#     print(list[i]**2,end=" ")
#     i=i+1

# list=[1,2,3]
# i=0
# while i<len(list):
#     j=0
#     while j<len(list):
#         k=0
#         while k<len(list):
#             if  i!=j and j!=i and k!=j and k!=i:
#                 print (list[i],list[j],list[k])
#             k=k+1
#         j=j+1
    # i=i+1
    
# name=[1,2,0,3,4,5,0,0,0]
# i=0
# b=[]
# c=[]
# while i<len(name):
#     if name[i]==0:
#         b.append(name[i])
#     else:
#         c.append(name[i])
#     i=i+1
# print(c,b)

num=int(input("enter your number...."))
i=1
c=0
while i<=(num):
    if (num)%i==0:
        c=c+1
    i=i+1
if c==2:
    print(num,"is a prime ")
else:
    print(num,"is not a prime number")

# a=[[1,2,3],[1,2,4,6]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     sum1=0
#     while j<len(a[i]):
#         sum=sum+(a[i][j])
#         sum1=sum1+(a[i][j])
#         j=j+1
#     i=i+1
# print(sum)
# print(sum1)

# a=[2,"4","-3",4.6,4,6]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+int(a[i])
#     i=i+1
# print(sum)


# list=[3, 40, 41, 43, 74, 9]
# i=0
# b=[]
# string=""
# while i>=-len(list):
#     b.append(list[i])
#     string=string+str(list[i])
#     i=i-1
# print(string)       

# a=[3, 40, 41, 43, 74, 9]
# string=""
# i=0
# while i<len(a):
#     string=string+str(a[i])
#     i=i+1
# print(string)

# a=['red', 'green', 'white', 'black']
# i=-1
# while i>=-len(a):
#     print(a[i])
#     i-=1

# number=[50,40,23,70,56,12,5,10,7]
# i=0
# count=0
# while i<len(number):
#     if number[i]>20 and number[i]<40:
#         count=count+number[i]
#     i=i+1
# print(count)

# a=['aabc', 'abc', 'ab', 'ha']
# i=0
# compare=str (a[0])
# compare=compare[0]
# while i<len(a):
#     element=str(a[i])
#     if element[0]!=compare:
#         Ans=True
#         break
#     ans=False
#     i=i+1
# print(ans)   
