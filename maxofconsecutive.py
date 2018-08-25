s=raw_int(input())
l=[int(x) for x in raw_input().split()]
for i in range(0,s-1):
	print max(l[i],l[i+1]),
