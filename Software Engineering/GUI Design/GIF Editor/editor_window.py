from tkinter import *
from tkinter import filedialog as fd
from PIL import Image


class GIFCanvas(Canvas):
    """
    An enhanced tk.Canvas with various features for editing GIFs
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layers = [self.new_layer()]
        self.selected_layer = self.layers[0]

        # EVENT LIST
        # https://www.tutorialspoint.com/list-of-all-tkinter-events

        # Paint Configs and Data
        self.paint_info = {
            'events': ['<B1-Motion>', '<1>'],
            'enabled': False,
            'mask': None,
            'size': 3,
            'color': '#fffffffff',
            'opacity': 1.0
        }

    def open_gif(self):
        import_filename = fd.askopenfilename()
        if import_filename.endswith('.gif'):
            im = Image.open(import_filename)
            return im
        else:
            raise ValueError('Incorrect filename to open a gif')

    def new_layer(self):
        """
        Creates a new layer TODO: update the GUI accordingly
        Returns:
            PIL.Image: A transparent image with the same dimensions as the canvas
        """
        return Image.new('RGBA', (self.winfo_width(), self.winfo_height()))

    def set_paint(self, enable: bool):
        """
        Enable/Disable the paint tool
        """
        self.paint_info['enabled'] = enable
        for event in self.paint_info['events']:
            if enable:
                self.bind(event, self.paint)
            else:
                self.unbind(event)

    def paint(self, event: Event):
        """
        Draws a brushstroke
        TODO: Edit a PIL Image instance instead of the canvas itself
        """
        x1, y1, x2, y2 = (event.x - self.paint_info['size']),\
                         (event.y - self.paint_info['size']),\
                         (event.x + self.paint_info['size']),\
                         (event.y + self.paint_info['size'])
        self.create_oval(x1, y1, x2, y2, fill=self.paint_info['color'], outline=self.paint_info['color'])

    @staticmethod
    def vertical_flip(img: Image.Image):
        """
        Flip a PIL.Image.Image object vertically
        """
        return img.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)

    @staticmethod
    def horizontal_flip(self, img: Image.Image):
        """
        Flip a PIL.Image.Image object horizontally
        """
        return img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)

    @staticmethod
    def copy_paste_box_select(self, im: Image.Image, bbox: tuple, left_top: tuple, vflip=False, hflip=False):
        frames = []
        for i in range(im.n_frames):
            im.seek(i)
            frame = im.convert('RGBA').copy()
            select = frame.crop(bbox)
            if vflip:
                select = self.vertical_flip(select)
            if hflip:
                select = self.horizontal_flip(select)
            Image.Image.paste(frame, select, left_top)
            frames.append(frame)
        return frames
