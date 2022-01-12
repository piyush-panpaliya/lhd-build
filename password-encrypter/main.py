import base64

class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def encode():
    print(bcolors.WARNING +"Hii this is a password encrypter pls input ur password"+ bcolors.ENDC)
    input1=input(bcolors.BOLD+"Whats thepassword?:"+ bcolors.ENDC).encode("utf-8")
    encoded = base64.b64encode(input1)
    print(bcolors.WARNING +f"Your encoded password is:{encoded}"+ bcolors.ENDC)

def decode(encoded):
    decoded = base64.b64decode(encoded)
    print(bcolors.WARNING +f"Your decoded password is:{decoded}"+ bcolors.ENDC)

def main():
    input3=int(input(bcolors.OKCYAN+"wanna 1)decode or 2)encode?: "+ bcolors.ENDC).encode("utf-8"))
    if input3==1:
        encode()
    elif input3 ==2:
        i4=input(bcolors.OKCYAN+"Enter the password u wanna decode "+ bcolors.ENDC).encode("utf-8")
        decode(i4)
    else:
        print(bcolors.WARNING +"invalid reply"+ bcolors.ENDC)

main()
