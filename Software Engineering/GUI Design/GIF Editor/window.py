import os
from tkinter import *


class TkEnhanced(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.temp_folder = 'temp'

		if not os.path.exists(self.temp_folder):
			os.mkdir(self.temp_folder)

	def cleanup(self):
		for file in os.listdir(self.temp_folder):
			os.remove(os.path.join(self.temp_folder, file))
		self.destroy()
