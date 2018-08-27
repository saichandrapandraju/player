n=input()
l=list(n)
for i in range(0,len(l)):
	if(l[i]==' '):
		l.remove(l[i])
	if(i+1==len(l)):
	            break
for i in range(0,len(l)):
	print(l[i],end='')
