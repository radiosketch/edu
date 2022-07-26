from tkinter import *
from tkinter import ttk

from editor_window import GIFCanvas
from dev_additions import GIFLabel


root = Tk()

root.title("GIF Editor")
root.iconbitmap('assets/GIF_E_128.ico')

# Tab Container (Notebook)
nbk = ttk.Notebook(root, width=400, height=400)
nbk.pack(pady=10, expand=True)

editor_nbk = ttk.Frame(nbk)
editor_nbk.pack(fill='both', expand=True)

settings_nbk = ttk.Frame(nbk)
settings_nbk.pack(fill='both', expand=True)

# Editor Tab Elements
canvas = GIFCanvas(editor_nbk, bg="black")
canvas.set_paint(True)
canvas.pack(fill='both', expand=True)

# Settings Tab Elements
ttk.Button(settings_nbk, text='Quit', command=root.destroy).grid(row=0, column=0)
ttk.Button(settings_nbk, text='Open Test', command=canvas.open_gif).grid(row=0, column=1) # Test Button, TODO Remove This Later
# GIFLabel(settings_nbk, image='assets/test.gif')

# Add Editor Tab to the Notebook
nbk.add(editor_nbk, text='Editor')
nbk.add(settings_nbk, text='Settings')

# # 1st Tab Container
# nbk1 = ttk.Frame(nbk)
# nbk1.pack(fill='both', expand=True)

# # 2nd Tab Container
# nbk2 = ttk.Frame(nbk)
# nbk2.pack(fill='both', expand=True)

# # 1st Tab Elements
# ttk.Entry(nbk1).grid(column=1, row=0)
# ttk.Button(nbk1, text='Open File', command=lambda: nbk.add(nbk2)).grid(column=1, row=1)
# ttk.Button(nbk1, text='New Tab').grid(column=1, row=2)

# # 2nd tab Elements
# ttk.Button(nbk2, text='Quit', command=root.destroy).grid(column=2, row=0)

# # Combine Tabs into Notebook
# nbk.add(nbk1, text='One')
# nbk.add(nbk2, text='Two')

# # Start with Tab #2 Hidden
# nbk.hide(1)


# WORKING EXAMPLE USAGE OF EXISTING METHODS
# WITHOUT GUI
# if __name__ == '__main__':
# 	gif = Image.open('in.gif')
# 	# bbox = (0, gif.height//2, gif.width, gif.height)
# 	bbox = (0, 0, gif.width//2, gif.height)
# 	left_top = (gif.width//2, 0)
# 	frames = copy_paste_box_select(
# 			gif,
# 			bbox,
# 			left_top,
# 			hflip=True
# 		)
# 	frames[0].save('out.gif',
# 		save_all=True,
# 		append_images=frames[1:],
# 		loop=0)

root.mainloop()
