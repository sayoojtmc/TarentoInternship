n,k=list(map(int,input().split(' ')))
lst=[]
lst = list(map(int,input().split(' ')))
lst.sort()
for j in range(k):
    lst[-1]=lst[-1]//2
    lst.sort()
print(sum(lst))