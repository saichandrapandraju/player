n=input()
l=list(n)
i=0
while(i<len(l)):
	t=l[i]
	l[i]=l[i+1]
	l[i+1]=t
	i+=2
for i in range(0,len(l)):
    print(l[i],end='')
