import math
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk


class GIFCanvas(Canvas):
    """
    An enhanced tk.Canvas with various features for editing GIFs
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layers = [self.new_layer()]
        self.selected_layer = self.layers[0]
        self.zoom = {
            'events': ['<MouseWheel>', '<Configure>'],
            'enabled': False,
            'val': 5
        }
        self.temp = {
            'background': 'temp/background.png'
        }

        # EVENT LIST
        # https://www.tutorialspoint.com/list-of-all-tkinter-events

        # Paint Configs and Data
        self.paint_info = {
            'events': ['<B1-Motion>', '<1>'],
            'enabled': False,
            'mask': None,
            'size': 3,
            'color': '#fffffffff',
            'opacity': 1.0,
            'previous position': None # For interpolating between positions
        }

        # Rectangle Select Configs and Data
        self.rect_sel_info = {
            'events': ['<B1-Motion>', '<1>'],
            'points': None, # (x1, y1, x2, y2)
            'enabled': False,
        }

    def open_gif(self):
        import_filename = fd.askopenfilename()
        if import_filename.endswith('.gif'):
            im = Image.open(import_filename)
            # Update the timeline and canvas with the new image
        else:
            raise ValueError('Incorrect filename to open a gif')

    def new_layer(self):
        """
        Creates a new layer TODO: update the GUI accordingly
        Returns:
            PIL.Image: A transparent image with the same dimensions as the canvas
        """
        return Image.new(
            'RGBA',
            (self.winfo_width(), self.winfo_height())
            )

    def update_layer(self, index):
        pass

    def set_layer_select(self, index):
        pass

    def enable_paint(self, enable: bool):
        '''
        Enable/Disable the paint tool
        '''
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
        size = self.paint_info['size']
        color = self.paint_info['color']
        prev_pos = self.paint_info['previous position']

        x1, y1, x2, y2 = (event.x - size),\
                         (event.y - size),\
                         (event.x + size),\
                         (event.y + size)

        if prev_pos and event.state == 264:
            # Draw a line between this point and the previous
            px, py = prev_pos
            if self.distance((px, py), (event.x, event.y)) > size:
                # Only if brush is moving too fast
                self.create_line(px, py, event.x, event.y, fill=color, width=size * 2 + 1)

        self.create_oval(x1, y1, x2, y2, fill=color, outline=color)

        self.paint_info['previous position'] = (event.x, event.y)

    def enable_zoom(self, enable: bool):
        '''
        Enable/Disable the zoom function
        '''
        self.zoom['enabled'] = enable
        for event in self.zoom['events']:
            if enable:
                self.bind(event, self.update_zoom)
            else:
                self.unbind(event)

    def update_zoom(self, event: Event):
        dz = 0
        if event.delta != 0:
            dz = event.delta//abs(event.delta)

        # Update the background image
        img = self.generate_background(delta_zoom=dz)
        self.delete(1)
        self.create_image(img.width() // 2, img.height() // 2, image=img)

    def generate_background(self, delta_zoom=0):
        '''
        Generate a grey checkerboard background as seen in a typical photo editor
        '''
        self.zoom['val'] = self.zoom['val'] + delta_zoom
        if self.zoom['val'] <= 0:
            self.zoom['val'] = 1

        zoom = self.zoom['val']

        self.update()

        width = zoom * math.ceil(self.winfo_width() / zoom)
        height = zoom * math.ceil(self.winfo_height() / zoom)

        u_width = math.ceil(width / zoom)
        u_height = math.ceil(height / zoom)

        img = Image.new(mode='RGB', size=(u_width, u_height))
        pixels = img.load()

        lg = 255 // 3 # Light Grey
        dg = 255 // 2 # Dark Grey
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixels[i, j] = (lg, lg, lg)
                temp = lg
                lg = dg
                dg = temp
            if img.size[1] % 2 == 0:
                temp = lg
                lg = dg
                dg = temp

        img = img.resize((width, height), Image.Resampling.BOX)
        img.save(self.temp['background'])
        return ImageTk.PhotoImage(Image.open(self.temp['background']))

    @staticmethod
    def distance(p1: tuple, p2: tuple):
        """
        Calculate the distance between two points in 2D space
        """
        return math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))

    @staticmethod
    def vertical_flip(img: Image.Image):
        """
        Flip a PIL.Image.Image object vertically
        """
        return img.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)

    @staticmethod
    def horizontal_flip(img: Image.Image):
        """
        Flip a PIL.Image.Image object horizontally
        """
        return img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)

    @staticmethod
    def copy_paste_box_select(im: Image.Image, bbox: tuple, left_top: tuple, vflip=False, hflip=False):
        """
        Copy & paste a box selection to a new point, specified by the top left point.
        """
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
