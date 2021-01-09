array=[]
def readList(rows,columns,array):
    for rowIndex in range(rows):
        column=[]
        for columnIndex in range(columns):
            element=input("enter the element in row "+str(rowIndex)+" and column "+str(columnIndex)+" ")
            column.append(element)
        array.append(column)
    return array

try:
    rows=int(input("enter the number of rows"))
    columns=int(input("enter the number of columns"))
    array=readList(rows,columns,array)
    print(array)
except ValueError:
    print("Kindly enter numbers only")