n,k=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,n):
	if(l[i]==k):
		print(i+1)
