class point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)
    def move(self):
        self.x += self.x
        self.y += self.y
p1 = point(5,7)
p1.move()
print("the points after moved are", p1.x, "and", p1.y)