class Color:
    def __init__(self, color):
        self._color = color
        
    def __str__(self):
        return f'Color: {self._color}'
    
    def get_color(self):
        print(f'El color es: {self._color}')
        
    def set_color(self, color):
        self._color = color