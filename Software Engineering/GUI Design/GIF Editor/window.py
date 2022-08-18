import os
from tkinter import *


class TkEnhanced(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def cleanup(self):
		dir = 'temp'
		for file in os.listdir(dir):
			os.remove(os.path.join(dir, file))
		self.destroy()
