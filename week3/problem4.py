# import random
# lst=[random.randint(1,100) for i in range(10)]
# print(lst)
# n=len(lst)
# for i in range(len(lst)):
#     for j in range(0,n-i-1):
#         if lst[j]>lst[j+1]:
#             lst[j],lst[j+1]=lst[j+1],lst[j]
# print(lst)
# print(lst[-2])

import random
lst=[50,78,85,45,65,89,80,89]
print(lst)
n=len(lst)
max=second=0
count=0
for i in range(n):
    if max<lst[i]:
        second=max
        max=lst[i]
    elif second<lst[i]<max:
        second=lst[i]
for i in lst:
    if i==max:
        count+=1
print(count)
if count>=2:
    print(max)
else:
    print(second)
    


