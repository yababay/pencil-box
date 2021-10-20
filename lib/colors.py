colors = {
    'красный': 'red',
    'желтый':  'yellow',
    'зеленый': 'green',
    'синий':   'blue'
}

def translate_color(color: str):
    return colors.get(color, 'grey')
