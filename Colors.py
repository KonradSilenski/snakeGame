# Color codes

class Colors:
    def getColor(color):
        return {
            'GREY': (128, 128, 128),    #GREY
            'RED': (255, 0, 0),         #RED
            'BLUE': (0, 255, 255),      #BLUE
            'GREEN': (25, 87, 0),       #GREEN
            'LGREEN': (25, 160, 0),     #LIGHT GREEN
            'DGREEN': (140, 160, 0),    #DARK GREEN
            'WHITE': (255, 255, 255)    #WHITE
        }.get(color, (128, 128, 128))
