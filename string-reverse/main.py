class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def reverse(i):
    array = i.split() 
    revArray =array[::-1]  
    space=" "
    revString= space.join(revArray)
    return revString

print(bcolors.WARNING +"Hii pls input the string u wanna reverse"+ bcolors.ENDC)
input=input(bcolors.BOLD+"your string:"+ bcolors.ENDC)

output=reverse(input)
print(f"{bcolors.OKCYAN}the reveresed string is:{bcolors.ENDC} {bcolors.OKGREEN}{bcolors.BOLD}{output}{bcolors.ENDC}{bcolors.ENDC}")
