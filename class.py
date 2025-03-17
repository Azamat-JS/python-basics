class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

RedCircle = Circle(4, 'yellow')
print(RedCircle)  # Now this prints: Circle(radius=10, color='red')
print(RedCircle.add_radius(2))
#=----------------------
# class Rectangle(object):
#     def __init__(self, color, height, width):
#         self.height = height
#         self.color = color
#         self.width = width

#     def __str__(self):
#         return f"Rectangle(parameter={(self.height + self.width)*2}, area={self.width * self.height})"
    
# BlueRectangle = Rectangle('blue',2, 4)
# print(BlueRectangle)


