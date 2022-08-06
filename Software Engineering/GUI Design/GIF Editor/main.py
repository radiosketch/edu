from tkinter import *
from tkinter import ttk

from window import TkEnhanced
from editor_window import GIFCanvas
from dev_additions import GIFLabel


root = TkEnhanced()

root.title("GIF Editor")
root.geometry('+300+300')
root.iconbitmap('assets/GIF_E_128.ico')
root.overrideredirect(True)

# Custom Title Bar
title_bar = Frame(root, bg='white', bd=1)
title_bar.pack(expand=True, fill=X)

title_label = Label(title_bar, text="GIF Editor")
title_label.pack(side=LEFT, pady=4)

exit_button = Button(title_bar, bg='red', command=root.destroy)
exit_button.pack(side=RIGHT, pady=4, padx=4)

window_button = Button(title_bar, bg='green', command=root.toggle_windowed)
window_button.pack(side=RIGHT, pady=4, padx=4)

minimize_button = Button(title_bar, bg='blue', command=root.minimize)
minimize_button.pack(side=RIGHT, pady=4, padx=4)

title_bar.bind('<B1-Motion>', root.move_app)
title_bar.bind('<1>', root.set_move_offset)
title_bar.bind('<Map>', root.frame_mapped)

# Tab Container (Notebook)
nbk = ttk.Notebook(root, width=400, height=400)
nbk.pack(pady=10, expand=True)

editor_nbk = ttk.Frame(nbk)
editor_nbk.pack(fill='both', expand=True)

settings_nbk = ttk.Frame(nbk)
settings_nbk.pack(fill='both', expand=True)

# Editor Tab Elements
toolbar = Frame(editor_nbk, width=50, bg='red')
toolbar.pack(fill='both', expand=True, side=LEFT)
canvas = GIFCanvas(editor_nbk, bg="black")
canvas.set_paint(True) # TODO Remove this once toolbar is implemented
canvas.pack(fill='both', expand=True)

# Settings Tab Elements
ttk.Button(settings_nbk, text='Quit', command=root.destroy).grid(row=0, column=0)
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
