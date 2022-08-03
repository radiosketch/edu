from tkinter import *


class TkEnhanced(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.drag_offset = (0, 0)

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

