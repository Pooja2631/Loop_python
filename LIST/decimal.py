number=[1,0,0,1,1,0,1,1]
i=len(number)-1
c=1
decimal =0
while i>=0:
       decimal=decimal+number[i]/c
       c=c/2
       i=i+1

