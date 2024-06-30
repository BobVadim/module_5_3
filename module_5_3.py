class House:
    def __init__(self, name, number_of_floors, ):
        self.number_of_floors = number_of_floors
        self.name = name

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            new_floor = list(range(1, new_floor + 1))
            print(self.name, *new_floor)

        return self.number_of_floors

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name},  Количество этажей: {self.number_of_floors}"
    def __eq__(self, other):
        return self.number_of_floors == other
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        return self.number_of_floors + value
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)



h1 = House('ЖК Эльбрус', 25)
h2 = House('ЖК Акация', 30)

h1.go_to(15)
h2.go_to(3)

print(len(h1))
print(len(h2))

print(str(h1))
print(str(h2))
print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)