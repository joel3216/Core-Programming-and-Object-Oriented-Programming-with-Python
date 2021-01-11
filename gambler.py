import random
stake=1
goal=200
wallet=1
losses=0

def gamble(wallet,stake,goal,losses):
    
    while(wallet>0 and wallet<goal):
        flipCoin=random.randrange(2)
        if flipCoin==0:
            wallet+=stake
        else:
            wallet-=stake
    
    if wallet==0:
        losses+=1
    
    return losses

try:
    maxGambles=int(input("enter the maximum number of times to run the experiment"))
    if maxGambles<=0:
        raise ValueError
    for instance in range(maxGambles):
        losses=gamble(wallet,stake,goal,losses)
        wins=maxGambles-losses
    winPercentage=wins/maxGambles*100
    lossPercentage=100-winPercentage

    print('''No.of Wins : '''+str(wins)+'''
    No.of Losses : '''+str(losses)+'''
    Win Percentage : '''+str(winPercentage)+'''
    Loss Percentage : '''+str(lossPercentage))
except ValueError:
    print("kindly enter a positive integer")