n,k=map(str,input().split())
n=list(n)
k=list(k)
c=0
for i in range(0,len(n)):
	if(n[i]!=k[i]):
		c+=1
if(c==1):
	print('yes')
else:
	print('no')
