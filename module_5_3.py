class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.number_of_floors = number_of_floors
        self.name = name

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            new_floor = list(range(1, self.new_floor + 1))
            print(self.name, *new_floor)

        return self.number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name},  Количество этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return other == self.number_of_floors

    def __ne__(self, other):
        return other != self.number_of_floors

    def __gt__(self, other):
        return other > self.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __del__(self):
        return print(f"{self.name} снесен но останется в истории!")


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Акация', 25)
h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)
print(h1 == h2)
print(h1 <= h2)
print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))
print(h1 != h2)
print(h1 > h2)
h1 = h1 + 10
print(h1)
h1.go_to(30)
h2.go_to(20)
h3.go_to(4)
del h2
del h3