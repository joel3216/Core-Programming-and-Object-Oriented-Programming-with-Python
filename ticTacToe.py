import random

def checkDiagonals(matrix,character):
    characterCount=0
    for index in range(len(matrix)):
        if matrix[index][index]==character:
            characterCount+=1
    if characterCount==len(matrix):
        return True
    else:
        characterCount=0
        columnIndex=0
        for rowIndex in reversed(range(len(matrix))):
            if matrix[rowIndex][columnIndex]==character:
                characterCount+=1
            columnIndex+=1
        if characterCount==len(matrix):
            return True
        else:
            return False

def checkHorizontal(matrix,character):
    for column in range(len(matrix)):
        characterCount=0
        for row in range(len(matrix)):
            if matrix[row][column]==character:
                characterCount+=1
        if characterCount==len(matrix):
            return True

def playTicTacToe(matrixSize):
    matrix=[['_']*matrixSize]*matrixSize
    computerHorizontalCheck=['o']*matrixSize
    userHorizontalCheck=['x']*matrixSize    
    userWin=False
    computerWin=False
    while (computerHorizontalCheck not in matrix and userHorizontalCheck not in matrix) or '_' not in matrix:
        
        userWin=checkDiagonals(matrix,'x')
        computerWin=checkDiagonals(matrix,'o')
        if bool(userWin):
            break
        elif bool(computerWin):
            break
        else:
            userWin=checkHorizontal(matrix,'x')
            computerWin=checkHorizontal(matrix,'o')
            if bool(userWin):
                break
            elif bool(computerWin):
                break
        
        for row in matrix:
            print(row)
        try:
            rowInput=int(input("enter row no"))
            columnInput=int(input("enter column no"))
            if rowInput<0 or columnInput<0:
                raise ValueError
            if rowInput>=matrixSize or columnInput>=matrixSize:
                raise IndexError
        except ValueError:
            print("kindly enter positive integers for rows and columns")
            continue
        except IndexError:
            print("kindly enter values within the boundary of the matrix")
            continue
        else:
            if matrix[rowInput][columnInput]!='_':
                print(str(rowInput)+","+str(columnInput)+" is already occupied, pick another spot")
                continue
            else:
                updateRow=matrix[rowInput].copy()
                updateRow[columnInput]='x'
                matrix[rowInput]=updateRow
                
                while(True):
                    row=random.randrange(len(matrix))
                    column=random.randrange(len(matrix))
                    if matrix[row][column]!='_':
                        continue
                    else:
                        updateRow=matrix[row].copy()
                        updateRow[column]='o'
                        matrix[row]=updateRow
                        break
    if userHorizontalCheck in matrix or bool(userWin):
        print("User Wins!")
    elif computerHorizontalCheck in matrix or bool(computerWin):
        print("Computer Wins!")
    else:
        print("Draw!")

try:
    matrixSize=int(input("enter the matrix size"))
    if matrixSize<0:
        raise ValueError
except ValueError:
    print("kindly enter a positive integer")
else:
    playTicTacToe(matrixSize)
