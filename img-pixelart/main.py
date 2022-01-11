from PIL import Image
import os

class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

directory = os.getcwd()
def pixelate(input_file_path, output_file_path, pixel_size):
    image = Image.open(directory+"\\"+input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )

    image.save(directory+"\\"+output_file_path)

print(bcolors.WARNING +"Hii pls input the image to wanna make pixel art from"+ bcolors.ENDC)
inputi=input(bcolors.BOLD+"your image name(with extension): "+ bcolors.ENDC)
number =input(bcolors.BOLD+"the level of Pixelation(any number): "+ bcolors.ENDC)
try:
    pixelate(inputi,"output"+number+".jpg",int(number))
except:
    print(bcolors.WARNING +"Unkown error occured"+ bcolors.ENDC)
