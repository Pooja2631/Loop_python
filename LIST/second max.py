a=[50,40,23,70,50,12,5,10,57]
i=0
mini=a[0]
while i<len(a):
    if a[i]<mini:
        mini=a[i]
    i=i+1
    j=0
    sec=a[mini]
    while j<len(a):
        if mini<a[j] and a[j]<sec :
            sec=a[j]
        j=j+1
print(mini)
print(sec)   
        
