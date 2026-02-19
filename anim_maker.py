filename = input("What's the file you want to create? : ")

#f = open(filename, 'r+')
#fcontent = f.read()

save = """\n*This file was created with anim_maker.py*\n"""

buffer = input("What's the size of your video? : ")
save = save + "%"+buffer+"% "

buffer = input("What's the size of a pixel? : ")
save = save + "@"+buffer+"@ "

buffer = input("How many frames does your animation have? : ")
save = save + "!"+buffer+"! "

print(save)
