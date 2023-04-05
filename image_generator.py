import os
from PIL import Image
im = Image.open("./images/ferrari.jpg")

im = im.convert("RGB")

width, height = im.size

# change the resolution of output from here
resolution = 80   # KEEP 75-85 FOR default display scaling
resolution_x = int((width/height)*resolution)

print(width, height)

resized_im = im.resize((resolution_x, resolution))

# resized_im.show()        #Uncomment to see the output image


def generate_map():
    map = []
    for y in range(resolution-1):
        x_map = []
        for x in range(resolution_x-1):
            rgb = resized_im.getpixel((x, y))
            x_map.append(get_average(rgb))
        map.append(x_map)
        x_map = 0
    return (map)


def get_average(tuple):
    avg = (tuple[0]+tuple[1]+tuple[2])/3
    return avg


def show_map(map):
    for y in map:
        for x in y:
            if x < 52:
                print(" ", end="")
            elif 52 < x <= 104:
                print(".", end="")
            elif 104 < x < 156:
                print("-", end="")
            elif 156 < x <= 208:
                print("*", end="")
            elif 208 < x <= 256:
                print("0", end="")
        print("\n", end="")


def save_map(map):
    output = str()
    for y in map:
        for x in y:
            if x < 52:
                output += (" ")
            elif 52 < x <= 104:
                output += (".")
            elif 104 < x < 156:
                output += ("-")
            elif 156 < x <= 208:
                output += ("*")
            elif 208 < x <= 256:
                output += ("0")
        output += ("\n")
    with open("output.txt", 'w') as file_object:
        file_object.write(output)
        print("Output generated Sucessfully!")


map = generate_map()
save_map(map)

# Opening the oputput text file using notepad
osCommandString = "notepad.exe ./output.txt"
os.system(osCommandString)
