from lib.canvas import create_canvas, draw_pencils


def main():

    p1 = 'green', 123, True
    p2 = 'red',   123, True
    p3 = 'red',   123, False
    pencils = [p1, p2, p3]

    window = create_canvas()
    draw_pencils(pencils)
    window.mainloop()
    

if __name__ == "__main__":
    main()
