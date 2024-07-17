import math

class Figure():

    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = []
        self.filled = False
        if self.sides_count == len(sides) and self.__is_valid_sides(*sides) == True:
            self.set_sides(*sides)
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)

        if isinstance(color, list and tuple) and len(color) == 3:
            self.set_color(color[0], color[1], color[2])

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <=255 and 0 <= g <=255 and 0 <= b <=255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r,g,b) == True:
            self.__color = [r,g,b]
            self.filled = True

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                if i < 0:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) == True:
            self.__sides.clear()
            for i in new_sides:
                self.__sides.append(i)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color,sides)
        self.__radius = self.get_radius()

    def get_radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return self.radius**2 * math.pi

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__height =self.get__height()

    def get__height(self):
        p = self.__len__() / 2
        return (2 * math.sqrt(p * (p - self.get_sides()[0]) *(p - self.get_sides()[1]) *(p - self.get_sides()[2]))) / self.get_sides()[0]

    def get_square(self):
        return (self.get_sides()[0] * self.__height) / 2

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        __side = sides * 12
        super().__init__(color, *__side)

    def  get_volume(self):
        return self.get_sides()[0]**3

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())
#
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# # Проверка объёма (куба):
print(cube1.get_volume())





