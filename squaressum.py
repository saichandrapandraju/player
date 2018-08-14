a=int(input())
sum=0
while(int(a)>=1):
	d=int(a)%10
	sum=sum+(d**2)
	a=int(a)//10
	if(a==0):
		print(sum)
