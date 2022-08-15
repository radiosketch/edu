from tkinter import Label
from PIL import Image, ImageTk
from itertools import count, cycle


class GIFLabel(Label):
	"""
	A Label that displays images, and plays them if they are gifs
	:im: A PIL Image instance or a string filename
	Credit to u/social_nerdtastic on Reddit:
	https://www.reddit.com/r/Tkinter/comments/kler90/how_can_i_use_a_gif_as_a_background_for_a/
	"""
	def __init__(self, *args, **kwargs):
		self.gifpath = None

		if 'image' in kwargs:
			self.gifpath = kwargs['image']
			del kwargs['image']

		super().__init__(*args, **kwargs)

		if self.gifpath:
			self.load(self.gifpath)

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
		self.frames = cycle(frames)

		try:
			self.delay = im.info['duration']
		except:
			self.delay = 100

		if len(frames) == 1:
			self.config(image=next(self.frames))
		else:
			self.next_frame()

	def unload(self):
		self.config(image=None)
		self.frames = None

	def next_frame(self):
		if self.frames:
			self.config(image=next(self.frames))
			self.after(self.delay, self.next_frame)
