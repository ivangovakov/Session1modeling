import random

from point import Point

class ColorPoint(Point):
    def __init__(self, x, y, color):
        #raise and exception if we try to have not a number
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        self.color=color
        super().__init__(x, y)

    def __str__(self):
        return f"({self.color}: {self.x}, {self.y})"

p=ColorPoint(4, 3, "red")
print(p.distance_orig())
print(p)
p.color=("rojo"
         "")

# p=ColorPoint(1,2,"red")
# print(p)
# colors=("red", "green", "blue", "yellow", "black", "magenta",
#         "cyan", "white", "burgundy", "periwinkle", "marsala")
# color_points=[]
# for i in range(10):
#     color_points.append(
#         ColorPoint(random.randint(-10, 10),
#                    random.randint(-10,10),
#                    random.choice(colors)))
#
# print(color_points)
# color_points.sort()
# print(colors)
