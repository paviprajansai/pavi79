p=int(input())
v=""
for i in range(1,n+1):
	if p%i==0:
		v=v+str(i)+" "
print(v.strip())		
