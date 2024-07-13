class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Укажите название")
        self._name = name
        if not isinstance(author, str):
            raise TypeError("Укажите автора")
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Cтраницы должны быть целыми числами")
        if pages <= 0:
            raise ValueError("Cтраницы не могут быть отрицательными")
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Введите длительность аудио книги")
        if duration <= 0:
            raise ValueError("Длительность аудио книги должна быть больше 0")
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"



