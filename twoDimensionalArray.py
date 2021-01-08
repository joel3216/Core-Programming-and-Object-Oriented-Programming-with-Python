m=int(input("enter the number of rows"))
n=int(input("enter the number of columns"))
array=[]
for i in range(m):
    col=[]
    for j in range(n):
        element=input("enter the element in row "+str(i)+" and column "+str(j)+" ")
        col.append(element)
    array.append(col)
print(array)