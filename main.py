import sys
from lib.canvas import create_canvas, draw_pencils


def main(pencils, test=False):

    window = create_canvas()
    draw_pencils(pencils)
    if test:
        return
    window.mainloop()
    

if __name__ == "__main__":

    p1 = 'красный',     5.3, True
    p2 = 'желтый',     15.3, True
    p3 = 'синий',      18.3, False
    p4 = 'непонятный', 20.0, False
    p5 = 'зеленый',    15.1, True

    pencils = [p1, p2, p3, p4, p5]

    try:

        """ Передаем в виде параметра, чтобы проверять main юниттестами. """
        main(pencils)

    except ValueError as verr:
        print(verr)
        sys.exit(1)
