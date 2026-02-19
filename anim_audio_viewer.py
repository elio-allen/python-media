# I have used random words for some variables so disregard their definitions
import pysine
from time import sleep
import re
import tkinter as tk
root = ""
display = int(input("GUI(1) or console(2)?:"))
fil = input("What animation do you want to open?: ")

freq = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
colortablehex = ["000000", "FFFFFF", "FF0000", "FF7F00", "FFFF00", "00FF00", "00FFFF", "0000FF", "4B0082", "8F00FF"]
colortabletext = ["\033[30m█","\033[97m█","\033[91m█","\033[33m█","\033[93m█","\033[92m█","\033[96m█","\033[94m█","\033[95m█","\033[35m█"]
delay = 1 / 30

chartable = [""]

fps_sel = input("Whats the FPS? (press enter for default (30))")
if (fps_sel != ""):
	delay = 1 / int(fps_sel)
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

x_frames = result.split('!')[1]

audio = result.split('#')[1]

store_audio = []

for i in audio:
        store_audio.append(i)

x_str, y_str = kill[0].split("x")  # split at the 'x'
y = int(y_str)
x = int(x_str)

s = re.sub(r'^%.*?%', '', result)
s = re.sub(r'^@.*?@', '', s)
s = re.sub(r'^!.*?!', '', s)
s = re.sub(r'^#.*?#', '', s)
print(s)

intList = [l for l in s.split("/") if l]


if display == 2:
    def console_frame(frame_id):
        for row_start in range(0, len(intList[frame_id]), x):
            row_chunk = intList[frame_id][row_start:row_start + x]
            # map each character to colortabletext and join
            line = "".join(colortabletext[int(c)] for c in row_chunk)
            print(line + "\033[0m")
    for i in range(0, int(x_frames)):
        print("\033[H\033[J")
        console_frame(i)
        pysine.sine(frequency=freq[int(store_audio[i])], duration=delay)
        

else:
    CELL_SIZE = int(pixel)

    # Create the window once
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CELL_SIZE * x, height=CELL_SIZE * y)
    canvas.pack()

    # Create rectangle grid once
    rectangles = [[None for _ in range(x)] for _ in range(y)]
    for row in range(y):
        for col in range(x):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            rect = canvas.create_rectangle(x1, y1, x2, y2, fill="#000000", outline="")
            rectangles[row][col] = rect

    total_frames = int(x_frames)
    delay_ms = int(delay * 1000)   # Tkinter uses milliseconds

    frame_id = [0]  # mutable list so inner function can update it

    def draw_frame():
        my_string = intList[frame_id[0]]

        index = 0
        for row in range(y):
            for col in range(x):
                color_index = int(my_string[index])
                hex_color = "#" + colortablehex[int(color_index)]
                canvas.itemconfig(rectangles[row][col], fill=hex_color)
                index += 1

        # move to next frame, loop back to 0
        frame_id[0] = (frame_id[0] + 1) % total_frames

        # schedule next frame
        root.after(delay_ms, draw_frame)

    draw_frame()      # start animation
    root.mainloop()   # start Tk event loop

