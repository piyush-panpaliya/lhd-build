import random 
import emoji
import time
class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# 1=rock 2=paper 3=scissor
def input1():
    try:
        i=input(emoji.emojize(bcolors.BOLD +"what are u gonna play?? 1):gem_stone: 2):newspaper:  3):scissors:  (write 1, 2 or 3): "+ bcolors.ENDC))
        return int(i)
    except:
        print(bcolors.WARNING +"invalid input"+ bcolors.ENDC)

def input2():
    retr= random.randint(1,3)
    print(retr)
    return retr

def calc(i1,i2):
    if i1==i2:
        return "draw"
    elif i1==1:
        if i2==2:
            return "loss"
        elif i2==3:
            return "win"
    elif i1==2:
        if i2==1:
            return "win"
        elif i2==3:
            return "loss"
    elif i1==3:
        if i2==1:
            return "loss"
        elif i2==2:
            return "win"
    else:
        return print(bcolors.WARNING +"Invalid option"+ bcolors.ENDC)

def show(r):
    if r=="win":
        print(bcolors.OKGREEN +"You won"+ bcolors.ENDC)
    elif r=="loss":
        print(bcolors.WARNING +"You lossed"+ bcolors.ENDC)
    elif r=="draw":
        print(bcolors.OKCYAN +"Its a draw"+ bcolors.ENDC)

def last():
    ans= input(bcolors.OKCYAN +"wanna play again(yes or no): "+ bcolors.ENDC)
    if ans=="yes":
        main()
    elif ans=="no":
        pass
    else:
        print(bcolors.WARNING +"invalid reply"+ bcolors.ENDC)
        last()

def main():
    i1=input1()
    i2=input2()
    result= calc(i1,i2)
    time.sleep(0.3)
    show(result)
    last()

main()
