import random
stake=1
goal=200
wallet=1
wins=0
losses=0

def gamble(wallet,stake,goal,wins,losses):
    
    while(wallet>0 and wallet<goal):
        flipCoin=random.randrange(2)
        if flipCoin==0:
            wallet+=stake
        else:
            wallet-=stake
    
    if wallet==0:
        losses+=1
    else:
        wins+=1
    
    return wins,losses

try:
    maxGambles=int(input("enter the maximum number of times to run the experiment"))
    for instance in range(maxGambles):
        wins,losses=gamble(wallet,stake,goal,wins,losses)

    winPercentage=wins/maxGambles*100
    lossPercentage=losses/maxGambles*100

    print('''No.of Wins : '''+str(wins)+'''
    No.of Losses : '''+str(losses)+'''
    Win Percentage : '''+str(winPercentage)+'''
    Loss Percentage : '''+str(lossPercentage))
except ValueError:
    print("kindly enter a positive integer")