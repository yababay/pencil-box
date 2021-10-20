from dataclasses import dataclass
from . settings import *
from . colors import translate_color


@dataclass
class Points:
    x1: int
    x2: int
    y2: int
    y1: int = pencil_padding


@dataclass
class Pencil:
    points: Points
    fill: str
    is_sharp: bool
    
    
def parse_pencils(pencils: tuple):

    if type(pencils) is not tuple:
        raise ValueError('"Карандаши" должны быть в кортеже.')

    pencil_with_gap = pencil_width + pencil_gap
    full_pencils_width = pencil_with_gap * len(pencils) - pencil_gap

    if full_pencils_width > canvas_width:
        raise ValueError('Карандашей слишком много или они слишком толстые.')

    """ Левая точка отрисовки карандашей """
    left_shift = int(canvas_width / 2 - full_pencils_width / 2)

    parsed = []

    for pencil in pencils:

        color, length, is_sharp = pencil

        if type(pencil) is not tuple:
            raise ValueError('Параметры должны быть в кортеже.')

        if type(color) is not str:
            raise ValueError('Параметр "цвет" должен быть строкой.')

        if type(length) not in [float, int]:
            raise ValueError('Параметр "длина" должен быть числом.')

        if type(is_sharp) is not bool:
            raise ValueError('Параметр "острый" должен быть логическим.')

        if length < pencil_min_length:
            raise ValueError('Слишком короткий карандаш в наборе.')
        if length > pencil_max_length:
            raise ValueError('Слишком длинный карандаш в наборе.')

        length *= pencil_cm
        color = translate_color(color)


        x1 = int(left_shift)
        x2 = int(x1 + pencil_width)
        y2 = int(pencil_padding + length)
        left_shift = x2 + pencil_gap
        points = Points(x1, x2, y2)
        
        parsed.append(Pencil(points, color, is_sharp))

    return tuple(parsed)
