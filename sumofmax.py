a=int(input())
list=[int(x) for x in input().split()]
c=sorted(list)
sum=0
for i in range(1,a):
	sum=sum+c[i]
print(sum)
