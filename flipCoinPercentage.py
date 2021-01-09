import random

headTally=0
tailTally=0
total=int(input("enter the number of times to flip the coin"))
if total>0:
    for i in range(total):
        flip=random.randrange(0,2)
        if flip==1:
            headTally+=1
        else :
            tailTally+=1
    headPercentage=(headTally/total)*100
    print("percentage of heads "+str(headPercentage))

    tailPercentage=(tailTally/total)*100
    print("percentage of tails "+str(tailPercentage))
else :
    print("the number has to be positive")