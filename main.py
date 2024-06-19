# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Book:  # Класс описывающий книгу
    def __init__(self, name: str, pages: (int, float), price: (int, float)):
        # Атрибуты
        self.name = name  # название
        self.pages = pages  # страницы
        self.price = price  # цена

        # инициализация атрибутов цены, названия и кол-ва страниц
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть int или float")
        if price < 0:
            raise ValueError("Цена не может быть отрицательным числом")
            self.price = price
        if not isinstance(pages, (int, float)):
            raise TypeError("Страницы должны быть int или float")
        if pages < 0:
            raise ValueError("Страниц не может быть отрицательное число")
            self.pages = pages
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")

    # Примеры
book1 = Book("Маленькая жизнь", 688, 1500)
book2 = Book("Черное воскресенье", 448, 250)
book3 = Book("Каллокаин", 256, 260)

def display(self):  # отображение информации о книге
    print("Название:", self.name)
    print("Страницы:", self.pages)
    print("Цена:", self.price)

def rent_pages(self, rent_pages: int):
    """
    Функция, показывающая сколько страниц было вырвано в книге
    :param rent_pages: количество вырванных страниц
    :return Количество оставшихся страниц
    """
    if not isinstance(rent_pages, int):
            raise TypeError("Количество вырванных страниц должно быть типом int")
        if rent_pages < 0:
            raise ValueError("Количество вырванных страниц должно быть больше ноля")

def __repr__(self):
    return f"Book({self.name},{self.pages},{self.price})"

class Car:  # класс описывающий машину
    def __init__(self, model_car, car_price: (int, float), car_color):
        # Атрибуты
        self.model_car = model_car  # модель
        self.car_price = car_price  # цена
        self.car_color = car_color  # цвет

        if not isinstance(model_car, str):
            raise TypeError("Марка машины должна быть типа str")
        if not isinstance(car_price, (int, float)):
            raise TypeError("Цена машины должна быть типа int или float")
            self.car_price = car_price
        if not isinstance(car_color, str):
            raise TypeError("Цвет машины должен быть типа str")
            self.car_color = car_color

# # Примеры инициализации
# car1 = Car("Chevrolet Camaro", 5000000, "Желтый")
# car2 = Car("ВАЗ-2106", 250000, "Красный")
# car3 = Car("jac", 3000000, "Белый")
def change_color(self, color: str):  # изменение цвета машины на синий
    """
   Функция, изменяющая цвет машины на другой
   :param self:
   :param color: синий
   Пример:
   >>>car1 = Car("Chevrolet Camaro", 5000000, "Желтый")
   >>>Car.change_color("Синий")
   """
    if not isinstance(color, str):
        raise TypeError("Новый цвет машины должен быть типа str")


def show_car_info(self):  # отображение информации о машине
    print("Модель:", self.model_car)
    print("Цена:", self.price)
    print("Цвет:", self.car_color)

class Scale:  # класс описывающий вес продуктов на весах
    def __init__(self, max_weight: Union[int, float], weight: Union[int, float]):
        # Атрибуты
        self.max_weight = max_weight
        self.weight = weight

        if not isinstance(max_weight, (int, float)):
            raise TypeError("Максимальный вес должен быть int или float")
        if max_weight <= 0:
            raise ValueError("Максимальный вес должен быть положительным")
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть int или float")
        if weight < 0:
            raise ValueError("Вес не должен быть отрицательным")

    # # Примеры инициализации
    # Scale1 = Scale(1000, 150)
    # Scale2 = Scale (470, 225)
    # Scale3 = Scale(500, 40)

    def add_weight(self, add_weight: Union[int, float]) -> None:
        """
        Добавление веса
        :param add_weight: Количество добавляемого веса
        :raise ValueError: Ошибка масса, добавляемая на весы, больше максимальной

        Пример:
        >>> scales = Scales(1000, 150)
        >>> scales.add_weight(200)
        """
        if not isinstance(add_weight, (int, float)):
            raise TypeError("Добавляемые вес должен быть int или float'")
        if add_weight < 0:
            raise ValueError("Добавляемый вес должен быть больше 0")

    def remove_weight(self, remove_weight: Union[int, float]) -> None:
        """
        Удаление веса с весов
        :param remove_weight: Удаляемый вес
        :raise ValueError: Ошибка масса, удаляемая с весов больше, чем масса, которая была на весах

        Примеры:
        >>> scales = Scales(100, 50)
        >>> scales.remove_weight_from_scales(45)
        """


if __name__ == "__main__":
    doctest.testmod()  # тестирование
