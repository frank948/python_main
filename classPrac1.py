import turtle

'''
class my_ski_gear:
    def __init__(self, skis, bindings, poles, boots, helmet):
        self.skis = skis
        self.bindings = bindings
        self.poles = poles
        self.boots = boots
        self.helmet = helmet

me = my_ski_gear('line-ninja', 'look-bindings', 'scott', 'dalbelo', 'giro-jackson')
'''
class Polygon:
    #initialize
    def __init__(self, sides, name, size=100, color='black',line_thickness=3):#method,can set parameters as default
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides-2)*180#anlges
        self.angle = self.interior_angles/self.sides


    #class method
    def draw(self):#pass in self to acces parameters
        turtle.pensize(self.line_thickness)
        turtle.color(self.color)
        for i in range(self.sides):
            turtle.fd(self.size)
            turtle.rt(180-self.angle)


class Square(Polygon):#subclass of Polygon
    def __init__(self, size=100, color='black',line_thickness=3):
            super().__init__(4,"Square", size, color, line_thickness)#super() takes from parent class
    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()

square = Square(color='#abc123')#defining a square using subclassing
print(square.draw())

#square = Polygon(4, 'Square', 100)
pentagon = Polygon(5, 'Pentagon', 100)
hexagon = Polygon(5, 'Hexagon',color='red',line_thickness=20)

#print(square.sides, square.name)
#print(pentagon.sides, pentagon.name)
#print(square.interior_angles)#360
#print(square.angle)#90

#square.draw()
#pentagon.draw()
#hexagon.draw()
turtle.done()