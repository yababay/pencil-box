from . settings import *
from dataclasses import dataclass

global y_top, y_bottom

y_top = pencil_padding
y_bottom = y_top + pencil_height


@dataclass
class Points:
    x1: int
    x2: int
    y1: int = y_top
    y2: int = y_bottom

@dataclass
class Pencil:
    points: Points
    fill: str
    length: float
    is_sharp: bool
    
class PencilBox:

    def __init__(self, pencils: list):
        full_pencils_width = (pencil_width + pencil_gap) * \
            len(pencils) - pencil_gap
        if full_pencils_width > canvas_width:
            raise ValueError('Карандашей слишком много '
                    'или они слишком толстые.')
        self.left_shift = canvas_middle - int(full_pencils_width / 2)
        self.pencils = list(map(lambda pencil: Pencil(self.get_next_points(), \
                *pencil), pencils))

    def get_next_points(self):
        x1 = self.left_shift
        x2 = x1 + pencil_width
        points = Points(x1, x2)
        self.left_shift = x2 + pencil_gap
        return points

    def get_pencils(self):
        return tuple(self.pencils)


