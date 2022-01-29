# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# sum1=0
# average=0
# average1=0
# count=0
# count1=0

# while i<len(elements):
#     if (elements[i])%2==0:
#         count=count+1
#         sum=sum+elements[i]
#         average=sum//count


#     else:
#         count1=count1+1
#         sum1=sum1+elements[i]
#         average1=sum1//count1
#     i=i+1
# print(average)
# print(average1)


n = 8
m = n+1
for i in range(n//2-1):
	for j in range(m):
		if i == n//2-2 and (j == 0 or j == m-1):
			print("\u2764\uFE0F", end=" ")
		elif j <= m//2 and ((i+j == n//2-3 and j <= m//4) \
							or (j-i == m//2-n//2+3 and j > m//4)):
			print("\u2764\uFE0F", end=" ")
		elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) \
						or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
			print("\u2764\uFE0F", end=" ")
		else:
			print(" ", end=" ")
	print()

for i in range(n//2-1, n):
	for j in range(m):
		if (i-j == n//2-1) or (i+j == n-1+m//2):
			print('\u2764\uFE0F', end=" ")
		elif i == n//2-1:
			if j == m//2-1 or j == m//2+1:
				print(' ', end=" ")
			elif j == m//2:
				print(' ', end=" ")
			else:
				print(' ', end=" ")
		else:
			print(' ', end=" ")
			
	print()