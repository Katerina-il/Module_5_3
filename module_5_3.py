from operator import eq, add

class House:

    def __init__(self, name, number_of_floors):
        """  Developer - не только разработчик  """
        self.name = name
        self.number = number_of_floors # количество этажей



    def go_to(self, new_floor):


        if new_floor > self.number or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number}"


    def __len__(self):
        return self.number

    def __eq__(self, other):
        return self.number == other.number

    def __add__(self, value):  # увеличивает кол - во этажей на переданное значение value, возвращает сам объект self.
        self.number += value
        return self

    def __radd__(self, value):
        return self + self.number + value

    def __iadd__(self, value):  # - работают так же как и __add_(возвращают результат его вызова)
        self.number += value
        return self

    def __lt__(self, other):
        return self.number < other.number

    def __le__(self, other):
        return self.number <= other.number

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __ne__(self, other):
        return self.number != other.number  # должны возвращать результаты сравнения

#
# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
#
# h1.go_to(5)
# h2.go_to(10)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

# __len__

print(len(h1))
print(len(h2))

print(eq(h1, h2))  # _eq_

add (h1, 10) # _add_

print(h1)
print(h1 == h2)

h1 = h1 + 10  # _iadd_

print(h1)

h2 = h2 + 10   # _radd_

print(h2)

print(h1 > h2)  # _gt_
print(h1 >= h2)  # _ge_
print(h1 < h2)  # _lt_
print(h1 <= h2)  # _le_
print(h1 != h2)  # _ne_

