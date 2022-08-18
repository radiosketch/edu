import os
from tkinter import *
from tkinter import ttk

from window import TkEnhanced
from editor_window import GIFCanvas
from additions import GIFLabel


root = TkEnhanced()
root.protocol('WM_DELETE_WINDOW', root.cleanup)

root.title("GIF Editor")
root.geometry('+300+300')
root.iconbitmap('assets/GIF_E_128.ico')

# ---------- Tab Container (Notebook) ----------
nbk = ttk.Notebook(root)
nbk.pack(pady=10, expand=True, fill='both')
# Editor Tab
editor_nbk = ttk.Frame(nbk)
editor_nbk.pack(fill='both', expand=True)
# Settings Tab
settings_nbk = ttk.Frame(nbk)
settings_nbk.pack(fill='both', expand=True)

# ---------- Editor Tab Elements ----------
# Toolbar: Tools are icon buttons
toolbar = Frame(editor_nbk, width=75, bg='#FFB7C3')
toolbar.pack(fill='y', expand=False, side=LEFT, pady=2)
# Canvas Background
canvas_bg = Frame(editor_nbk, bg='black')
canvas_bg.pack(fill='both', expand=True, padx=2, pady=2)
# GIF Canvas
canvas = GIFCanvas(canvas_bg, bg="black", width=400, height=400, highlightthickness=0)
canvas.enable_paint(True) # TODO Remove this once toolbar is implemented
canvas.enable_zoom(True)
canvas.pack(expand=True, anchor='center')
# Timeline
timeline = Frame(editor_nbk, height=50, bg='#BCF4DE')
timeline.pack(fill='x', expand=False, padx=2)

# ---------- Settings Tab Elements ----------
ttk.Button(settings_nbk, text='Quit', command=root.cleanup).grid(row=0, column=0)
GIFLabel(settings_nbk, image='assets/test.gif').grid(row=0, column=1)

# ---------- Add Editor Tab to the Notebook ----------
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
