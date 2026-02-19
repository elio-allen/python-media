# I have used random words for some variables so disregard their definitions

import re
import tkinter as tk
root = ""
display = int(input("GUI(1) or console(2)?:"))
fil = input("What image do you want to open?: ")

colortablehex = ["000000", "FFFFFF", "FF0000", "FF7F00", "FFFF00", "00FF00", "00FFFF", "0000FF", "4B0082", "8F00FF"]
colortabletext = ["\033[30m█","\033[97m█","\033[91m█","\033[33m█","\033[93m█","\033[92m█","\033[96m█","\033[94m█","\033[95m█","\033[35m█"]


chartable = [""]

colortable_sel = input("Where's the colortable file? (press enter for default)")
if (colortable_sel != ""):
	# piss = Post-Intercontinental Sushi Strike
	piss = open(colortable_sel, 'r')
	colortablehex = piss.read()
	colortabletext = piss.read()
	piss.close()

f = open(fil, 'r')
# poo = Party of the Orphaned Orphans
poo = f.read()
text = poo

#removes asterisks(and contents) to remove comments
result = re.sub(r"\*.*?\*", "", text)
# removes newlines and spaces so parsing data is easier for me
result = re.sub(r"\s+", "", result)
print(result)

#Kilo-Illushins per Long Leopard
kill = result.split('%')[1:2]  # take first two parts
#Playing Inside a Xylophone Everytime i Live
pixel = result.split('@')[1]

x_str, y_str = kill[0].split("x")  # split at the 'x'
y = int(y_str)
x = int(x_str)

s = re.sub(r'^%.*?%', '', result)
s = re.sub(r'^@.*?@', '', s)

if display == 2:
    # go row by row
    for row_start in range(0, len(s), x):
        row_chunk = s[row_start:row_start + x]
        # map each character to colortabletext and join
        line = "".join(colortabletext[int(c)] for c in row_chunk)
        print(line + "\033[0m")
else:
    # Example string, must match total number of squares: x * y
    my_string = s  # length must equal x*y

    CELL_SIZE = int(pixel)
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CELL_SIZE * x, height=CELL_SIZE * y)
    canvas.pack()

    rectangles = [[None for _ in range(x)] for _ in range(y)]

    # Fill the board based on my_string
    index = 0
    for row in range(y):
        for col in range(x):
            color_index = int(my_string[index])
            hex_color = "#" + colortablehex[color_index]
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            rect = canvas.create_rectangle(x1, y1, x2, y2, fill=hex_color, outline="")
            rectangles[row][col] = rect
            index += 1
if root == "":
    quit()
root.mainloop()            
