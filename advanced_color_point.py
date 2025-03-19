from color_point import ColorPoint

class AdvancedPoint(ColorPoint):
    COLORS=["red", "blue", "green", "yellow", "black", 'white', "periwinkle"]
    def __init__(self, x, y, color):
        if color not in self.COLORS:
        # raise and exception if we try to have not a number
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        self._x=x
        self._y=y
        self._color=color

    @classmethod
    def add_color(cls, color):
        """
        adds a new color for our classes
        """
        cls.COLORS.append(color)
    @staticmethod
    def from_tuple (coordinate, color="red"):
        """
        creates a new point from a tuple rather than 2 individual values
        """
        x,y=coordinate
        return AdvancedPoint(x, y, color)
    @staticmethod
    def distance_2_points(p1, p2):
        return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0,5
    def distance_to_other(self, p):
        return ((self.x-p.x)**2+(self.y-p.y)**2)**0,5
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def color(self):
        return self._color
    @x.setter
    def x(self, value):
         self._x=value

    @y.setter
    def y(self, value):
         self._y=value

    @color.setter
    def color(self, value):
         self._color=value
AdvancedPoint.add_color("rojo")
p=AdvancedPoint(1,2,"rojo")
print(p)
print(p.distance_orig())
p2=AdvancedPoint.from_tuple((2, 3))
print(p2)
print(AdvancedPoint.distance_2_points(p2,p))
print(p.distance_to_other(p2))
print(p.x)
