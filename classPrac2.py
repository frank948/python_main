import matplotlib.pyplot as plt

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):#overloading operators allows operating of different types to class
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x,y)
        else:
            x = self.x + other
            y = self.y + other
            return Point(x,y)

    def plot(self):
        plt.scatter(self.x, self.y)

#a = Point(4,5)
#a.plot()

a = Point(0,2)
d = a + 5
print(d.x, d.y)

#plt.show()
#point1 = Point(4,5)
#print(point1.x)
