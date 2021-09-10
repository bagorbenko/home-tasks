import math
class WinDoor:
    def __init__(self, w, h, name):
        self.w = w
        self.h = h
        self.name = name

    def __repr__(self):
        return f'{self.name} {self.w}*{self.h}'

    def windSquare(self):
        wind_squre = self.w * self.h
        return wind_squre

class Room:
    def __init__(self, x, y, z):
        self.x = x  #width
        self.y = y  #length
        self.z = z  #high
        self.wd = [] #windows & doors

    def roomSquare(self):
        room_square = (self.x +self.y) * self.z * 2
        return room_square

    def addWD(self, new_windoor):
        self.wd.append(new_windoor)

    def workSurface(self):
        new_square = self.roomSquare()
        for i in self.wd:
            new_square -= i.windSquare()
        return new_square


class Wallpappers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pappersValue(self):
        value = (self.x * self.y)
        return value

j = Room(10, 5, 3)
j.addWD(WinDoor(2, 1, 'pupa'))
j.addWD(WinDoor(2.2, 0.8, 'lupa'))
w = Wallpappers(6.25, 0.8)
j = Room(10, 5, 3)
j.addWD(WinDoor(2, 1, 'pupa'))
j.addWD(WinDoor(2.2, 0.8, 'lupa'))
j.addWD(WinDoor(3, 1.5, 'zupa'))
print('Площадь команты', j.roomSquare())
print('Рабочее пространство', j.workSurface())
print('Количество необходимых обоев с запасом', math. ceil(j.workSurface()/w.pappersValue()))
