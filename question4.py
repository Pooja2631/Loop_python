# i=1
# sum=0
# while i<=11:
#     weight = int(input("enter the weight"))
#     sum=sum+i
#     i+=1
#     if weight%5==0:
#         continue
#     print(sum)

 
# num=input("enter your hashsd number")
# num=int(num)
# num=n=num
# ans=0
# while (num!=0):
#     dig=num%10
#     ans=ans+10
#     num=int(num/10)
# if(num%  ans==0):
#     print("enter the hashad number!")
# else:
    # print("it is not hashad number!")
 
fruits=["apple","banana","guava","carrot"]
fruits.append("pineapple")
print(fruits)

print(len(fruits))

fruits.clear()
print(fruits)

fruits.insert(3,"custardapple")
print(fruits)

fruits.pop(2)
print(fruits)


vegetables=["onion","potato","radish"]
fruits.extend(vegetables)
print(fruits)

fruits.reverse()
print(fruits)