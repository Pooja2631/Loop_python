# marks=[
# [78,76,94,86,88],
# [91,71,98,65],
# [95,45,78],
# [87,67,49,68,88]
# ]
# i=0
# sum=0
# while i<len(marks):
#     j=0
#     while j<len(marks[i]):
#         sum=sum+(marks[i][j])
#         j=j+1
#     i=i+1
# print(sum)        


# list=[2,3,[5,6,8,[2,3],6],8,9]
# print(list[2][0])
# print(list[2][2])
# print(list[2][3][1])
# print(list[2][4])
# print(list[3])



# list=[18,[2,3,4],14,15,[6,11,18],1,9,[25,10,6]]
# print(list[0])
# print(list[1][1])
# print(list[4][1])
# print(list[6])
# print(list[7][0])
# print(list[7][2])

# list=[[[2,1,8],[98,[48,5]],[9,17,10],7,22]]
# print(list[0][0][1])
# print(list[0][1][0])
# print(list[0][1][1][0])
# print(list[0][2][1])
# print(list[0][2][2])
# print(list[0][4])

# list=[[2,1,8],[98,[48,5]],[9,17,10],7,22]
# print(list[0][-2])
# print(list[1][-0])
# print(list[1][1][-0])
# print(list[2][-2])
# print(list[2][-1])
# print(list[0][-0])

# a=[[[2,4,5],[9,8,[48,7,6],40,1],9,10,11]]
# print(a[0][0][1])
# print(a[0][1][1])
# print(a[0][1][2][0])
# print(a[0][1][3])
# print(a[0][1][4])
# print(a[0][3])

# a=[[[48,44,9,],[7,4,2,3],[1,12,13,15,],4,2,[42,1,]]]
# print(a[0][0][1])
# print(a[0][0][2])
# print(a[0][1][1])
# print(a[0][5][0])
# print(a[0][1][2])

# a=[[9,[4,8,3,],[18,1,2,5,6,],[92,6,[26,8]]]]
# print(a[0][1][1])
# print(a[0][2][0])
# print(a[])


# list=[[1,2,[4,5,8],10,15,[7,8,[4,10,15]],20]]
# print(list[0][1])
# print(list[0][2][1])
# print(list[0][4])
# print(list[0][5][1])
# print(list[0][5][2][1])
# print(list[0][6])

# list=["a","b",["c",["d","e"],["j","g"],"k"],"l","m","n"]
# print(list[1])
# print(list[2][0])
# print(list[2][1][0])
# print(list[2][2][0])
# print(list[2][3])
# print(list[3][0])
# print(list[5][0])

# list = [["a"], ["b", "c"], ["d", "e", "f", "g"]]
# one_list = [num for sublist in list for num in sublist]
# print(one_list)

list=["a","b",["c",["d","e"],["j","g"],"k"],"l","m","n"]
i=0
a=[]
while i<len(list):
    j=0
    while j<len(list[i]):
        print(list[i][j])
        a.append(list)
        print(a)
        j=j+1
        i=i+1

