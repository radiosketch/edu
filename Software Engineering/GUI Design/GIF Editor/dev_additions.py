from tkinter import Label
from PIL import Image, ImageTk
from itertools import count, cycle

class GIFLabel(Label):
	"""
	A Label that displays images, and plays them if they are gifs
	:im: A PIL Image instance or a string filename
	https://www.reddit.com/r/Tkinter/comments/kler90/how_can_i_use_a_gif_as_a_background_for_a/
	"""
	def load(self, im):
		if isinstance(im, str):
			im = Image.open(im)
		frames = []

		try:
			for i in count(1):
				frames.append(ImageTk.PhotoImage(im.copy()))
				im.seek(i)
		except EOFError:
			pass

