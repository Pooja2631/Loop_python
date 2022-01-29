# ms=[[8,3,4],
#     [1,5,9],
#     [6,7,2]]
# i=0
# sum=0
# sum1=0
# sum2=0
# c1=0
# c2=0
# c3=0
# while i<len(ms):
#     sum=sum+ms[i][0]
#     sum1=sum1+ms[i][1]
#     sum2=sum2+ms[i][2]
#     i=i+1
# print('total of row 1 =',sum)
# print('total of row 2 =',sum1)
# print('total of row 3 =',sum2)


# ms=[[8,1,6],
#     [3,5,9],
#     [4,9,2]]
# i=0
# sr=0
# sc=0
# while i<len(ms):
#     j=0
#     sc=sc+ms[i][j]
#     sr=sr+ms[j][i]
#     i=i+1
# print(sr)
# print(sc)
# c=0
# d=0
# f=(len(ms)-1)
# d1=0
# d2=0
# while c<len(ms):
#     d1=d1+ms[c][d]
#     d2=d2+ms[c][f]
#     c+=1
#     d+=1
#     f-=1
# print(d1)
# print(d2)
# if sc==sr==d1==d2:
#     print(ms)