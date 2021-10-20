canvas_width   = 1024
canvas_height  = 800
canvas_background = '#dddddd'

pencil_width      = 60
pencil_semi_width = int(pencil_width / 2)
pencil_height     = int(canvas_height * .7)
pencil_padding    = int((canvas_height - pencil_height) / 2)
pencil_gap        = pencil_width / 2

""" Пикселей на сантиметр. """
pencil_min_length = 5
pencil_max_length = 20
pencil_cm         = int(pencil_height / pencil_max_length)

