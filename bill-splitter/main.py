class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def inputf():
    print(bcolors.WARNING +"Hii this is a bill splitter"+ bcolors.ENDC)
    input1=input(bcolors.BOLD+"What is the total bill?:"+ bcolors.ENDC)
    input2=input(bcolors.BOLD+"How many people are splitting the bill?: "+ bcolors.ENDC)
    return [int(input1),int(input2)]

def calc(i1,i2):
    return (round(float((i1/ i2))))

def show(pay):
    print(f"{bcolors.OKCYAN}Each person owes:{pay}{bcolors.OKCYAN}")

def main():
    [input1,input2]=inputf()
    pay = calc(input1,input2)
    show(pay)

main()