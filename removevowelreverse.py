n=int(input())
s=input()
l=list(s)
v=['a','e','i','o','u']
for i in range(0,n):
	if(l[i] in v):
		l[i]=''
c=l[::-1]
for i in range(0,len(c)):
	print(c[i],end='')
		
