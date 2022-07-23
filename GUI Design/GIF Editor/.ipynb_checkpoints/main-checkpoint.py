from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image

root = Tk()

root.title("GIF Manipulator")
root.geometry('400x300')


def open_gif():
	global im

	import_filename = fd.askopenfilename()
	if import_filename.endswith('.gif'):
		im = Image.open(import_filename)
	else:
		raise ValueError('Incorrect filename to open a gif')

	return im


def vertical_flip(img: Image.Image):
	return img.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)


def horizontal_flip(img: Image.Image):
	return img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)


def copy_paste_box_select(im: Image.Image, bbox: tuple, left_top: tuple, vflip=False, hflip=False):
	frames = []
	for i in range(im.n_frames):
		im.seek(i)
		frame = im.convert('RGBA').copy()
		select = frame.crop(bbox)
		if vflip:
			select = vertical_flip(select)
		if hflip:
			select = horizontal_flip(select)
		Image.Image.paste(frame, select, left_top)
		frames.append(frame)
	return frames


# Tab Container (Notebook)
nbk = ttk.Notebook(root, width=400, height=280)
nbk.pack(pady=10, expand=True)

# 1st Tab Container
nbk1 = ttk.Frame(nbk)
nbk1.pack(fill='both', expand=True)

# 2nd Tab Container
nbk2 = ttk.Frame(nbk)
nbk2.pack(fill='both', expand=True)

# 1st Tab Elements
ttk.Entry(nbk1).grid(column=1, row=0)
ttk.Button(nbk1, text='Open File').grid(column=1, row=1)

# 2nd tab Elements
ttk.Button(nbk2, text='Quit', command=root.destroy).grid(column=2, row=0)

# Combine Tabs into Notebook
nbk.add(nbk1, text='One')
nbk.add(nbk2, text='Two')

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
