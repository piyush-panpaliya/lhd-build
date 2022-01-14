class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def func(i):
    numb = [int(x) for x in i.split(",")]
    numb.sort()
    return ' , '.join([str(x) for x in numb])

print(bcolors.WARNING +"Hii this is a list sorter"+ bcolors.ENDC)
input1=input(bcolors.BOLD+"Input the list items seperated by coma and no spaces:"+ bcolors.ENDC)
print(bcolors.BOLD+"your sorted list is:"+bcolors.ENDC+bcolors.OKCYAN+str(func(input1)) +bcolors.ENDC)