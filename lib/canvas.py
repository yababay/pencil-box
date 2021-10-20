from tkinter import Tk, Canvas
from . settings import canvas_width, canvas_height
from . pencils  import parse_pencils
from . settings import pencil_width, canvas_background


global canvas


def create_canvas(title='Коробка с карандашами', 
        width=canvas_width, height=canvas_height):
    root = Tk()
    root.title(title)
    global canvas
    canvas = Canvas(root, width=width, height=height, bg=canvas_background)
    canvas.pack()
    return root


def draw_pencils(pencils: list):
    global canvas
    for pencil in parse_pencils(pencils):

        """ Четверть толщины. """
        q  = int(pencil_width / 4)

        x1 = pencil.points.x1
        x2 = pencil.points.x2
        y1 = pencil.points.y1
        y2 = pencil.points.y2 - pencil_width * 2

        """ Внешний прямоугольник. """
        canvas.create_rectangle(x1, y1, x2, y2, fill=pencil.fill)

        """ Внутренний прямоугольник. """
        x3 = x1 + q 
        x4 = x2 - q 
        canvas.create_rectangle(x3, y1, x4, y2, fill=pencil.fill)

        """ Сужающаяся часть. """
        y3 = y2 + pencil_width
        canvas.create_polygon(x1, y2, x3, y3, x4, y3, x2, y2, fill='white', outline='black')

        """ Острый грифель. """
        y4 = y3 + pencil_width
        x5 = int(x1 + pencil_width / 2)

        canvas.create_polygon(x3, y3, x5, y4, x4, y3, fill='black', outline='black')

        if pencil.is_sharp:
            continue

        """ Затупленный грифель. """
        canvas.create_rectangle(x1, y3 + q * 2, x2, y4, fill=canvas_background, outline=canvas_background)

