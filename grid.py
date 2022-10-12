from pixel import Pixel

class PixelGrid:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        self.pixels = []

        
    def create_grid(self) -> None: #resets the grid
        self.pixels = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append( self.default_pixel(x, y) )
            self.pixels.append(row)

    
    def default_pixel(self, x, y) -> Pixel: #can be overridden to change default pixel attributes like color or add a gradient
        return Pixel(x, y, 255)