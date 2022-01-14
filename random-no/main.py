import random

class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

number =["0","1","2","3","4","5","6","7","8","9"]
number2 =["1","2","3","4","5","6","7","8","9"]

def func(i):
    k=0
    for f in range(0,int(i)):
        if 0 == 1:
            k=int(str(k)+random.choice(number2))
        k=int(str(k)+random.choice(number))
    return k

print(bcolors.WARNING +"Hii this is a random no generator"+ bcolors.ENDC)
input1=input(bcolors.BOLD+"no of digits you want:"+ bcolors.ENDC)
print(bcolors.BOLD+"your random no is:"+bcolors.ENDC+bcolors.OKCYAN+str(func(input1)) +bcolors.ENDC)

