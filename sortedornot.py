n=int(input())
l=[int(x) for x in input().split()]
if(l==sorted(l)):
	print('yes')
else:
	print('no')
