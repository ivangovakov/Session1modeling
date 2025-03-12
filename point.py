import random


class Point:
    def __init__(self, x, y):
        '''
        Initialize a Point object
        :param x: the x position on the axis
        :param y: the y position on the axis
        '''
        self.x=x #define x attribute via self.x
        self.y=y #and assign the value x to it

    def __str__(self):
        """
        Magic Method that is called when we try to print on instance
        :param self:
        :return: Point (x,y)
        """

        return f"Point ({self.x}, {self.y})"
    def __repr__(self):
        return self.__str__() #use the same way of printing as str

    def distance_orig(self):
        return(self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        my_distance=self.distance_orig()
        other_distance=other.distance_orig()
        return my_distance>other_distance
    def __eq__(self, other):
        my_distance=self.distance_orig()
        other_distance=other.distance_orig()
        return my_distance==other_distance


if __name__ == "__main__":


    #now we need to instantiate it
    p=Point(1, 2)
    p2=Point(2,3)
    p4=Point(4.4,-55)
    print(f"p.x={p.x} and p.y={p.y}")
    print(f"p4.x={p4.x} and p4.y={p4.y}")
    p.x=20
    print(f"p.x={p.x} and p.y={p.y}")
    print(p)
    points=[]
    for i in range(5):
        points.append(Point(random.randint(-10,10),
                            random.randint(-10,10)))
    print("I got 5 random points")
    for p in points:
        print(p)

    print(p.distance_orig())
    print(f"I am comparing p>p2: {p>p2}") #I expect to have true
    print(f"I am comparing p=p2: {p==p2}")
    print("the sorted list of points is:")
    points.sort()
    print(points)