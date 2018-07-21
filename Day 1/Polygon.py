class Polygon:

    #def __init__(self):
    list_points= []
    def __init__(self, x, y):
        self.list_points.append([x, y])

    def perimeter(self):
        list_points = self.list_points
        a = 0
        answer = 0
        while a < len(list_points) - 1:
            answer1 = ((list_points[a][0] - list_points[a+1][0])**2 + (list_points[a][1] - list_points[a+1][1])**2)**0.5
            a += 1
            answer = answer1 + answer
        return abs(answer)

    def area(self):
        list_points = self.list_points
        x = 0
        answer = 0
        list_points.append(list_points[0])
        while x < len(list_points) - 1:
            answer1 = list_points[x][0]*list_points[x+1][1] - list_points[x+1][0] * list_points[x][1]
            x = x + 1
            answer = answer1 + answer
        return abs(answer) / 2
p1 = Polygon(2, 6)
p2 = Polygon(4, 6)
p3 = Polygon(4, 4)
p4 = Polygon(2, 4)
print(p4.area())
print(p4.perimeter())
