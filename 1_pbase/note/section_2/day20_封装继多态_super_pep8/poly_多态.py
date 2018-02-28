

class Shape:  # 图形类
    def draw(self):
        self.drawSelf()


class Point(Shape):
    def drawSelf(self):
        print("正在画一个点!")


class Circle(Point):
    def drawSelf(self):
        print("正在画一个圆")

shape = Point()
shape.draw()

shape = Circle()
shape.draw()





