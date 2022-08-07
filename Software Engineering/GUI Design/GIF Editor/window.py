from tkinter import *


class TkEnhanced(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.drag_offset = (0, 0)
		self.windowed = False
		self.window_size = (500, 500)
		self.window_position = (300, 300)

	def set_move_offset(self, event):
		"""
		Set the mouse position that the window is being dragged from.
		Use this method with .bind('<1>', root.set_move_offset)
		"""
		self.drag_offset = (event.x, event.y)

	def move_app(self, event):
		"""
		Move the application window.
		Use this methods with .bind('<B1-Motion>', root.move_app),
		and in combination with set_move_offset.
		"""
		self.geometry(f'+{event.x_root - self.drag_offset[0]}+{event.y_root - self.drag_offset[1]}')
		self.window_position = self.winfo_geometry().split('+')[1:]

	def frame_mapped(self, event):
		self.overrideredirect(True)
		self.update_idletasks()
		self.state('normal')

	def minimize(self):
		self.overrideredirect(False)
		self.update_idletasks()
		self.state('iconic')

	def toggle_windowed(self):
		if not self.windowed:
			geometry = self.winfo_geometry().split('+')
			geo_wh = geometry[0].split('x')
			self.window_size = (geo_wh[0], geo_wh[1])
			self.window_position = (geometry[1], geometry[2])


			screen_width = self.winfo_screenwidth()
			screen_height = self.winfo_screenheight()

			self.geometry(f'{screen_width}x{screen_height}+0+0')
			self.windowed = True
			print(self.window_size, self.window_position, self.windowed)
		else:
			self.geometry(f'{self.window_size[0]}x{self.window_size[1]}+{self.window_position[0]}+{self.window_position[1]}')
			self.windowed = False
			print(self.window_size, self.window_position, self.windowed)
