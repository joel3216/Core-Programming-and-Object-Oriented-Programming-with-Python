n=int(input("enter the number of elements"))
print("enter the elements")

a=[]
zeroSum=[]
for i in range(n):
    a.append(int(input()))

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if a[i]+a[j]+a[k]==0:
                zeroSum.append(str(a[i])+","+str(a[j])+","+str(a[k]))
                break
        
print(zeroSum)