"""
 Module. Product. Exercise of Programming 2 and Static Analysis 5.2
 @Motive . Static Analysis using Pylint and Flake8 – PEP 8
 @author . Ronald Sandí Quesada
 @Student-ID . A01794620
 @email . A01794620@tec.mx
 @MNA Class . Pruebas de Software y Aseguramiento de la Calidad (TC4017)
 @Professor . PhD Gerardo Padilla Zárate
 @Professor Evaluator and Tutor . PhD Daniel Flores Araiza
 @Period . I Trimester 2026
 @Date: 15 February 2026
"""


import math


class Product:

    """
    Product. It is a module which handles all features linked to the entity Product.
    The products are the essentials units for the POS system.
    """

    def __init__(self, dict_line):
        self.title = str(dict_line['title'])
        self.type = str(dict_line['type'])
        self.description = str(dict_line['description'])
        self.filename = str(dict_line['filename'])
        self.height = str(dict_line['height'])
        self.width = str(dict_line['width'])
        self.price = float(dict_line['price'])
        self.rating = str(dict_line['rating'])

    def __str__(self):
        return (f"Product details:\n"
                f"Title       := {self.title}\n"
                f"Price       := {self.price}\n"
                f"Type        := {self.type}\n"
                f"Description := {self.description}\n"
                f"Filename    := {self.filename}\n"
                f"Dimensions  := {self.height}h × {self.width}w\n"
                f"Rating      := {self.rating}\n"
                )

    @property
    def title(self):
        return f"{self._title}"

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value

    @property
    def type(self):
        return f"{self._type}"

    @type.setter
    def type(self, value):
        if not value:
            raise ValueError("Type cannot be empty")
        self._type = value


    @property
    def description(self):
        return f"{self._description}"

    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Description cannot be empty")
        self._description = value

    @property
    def filename(self):
        return f"{self._filename}"

    @filename.setter
    def filename(self, value):
        if not value:
            raise ValueError("Filename cannot be empty")
        self._filename = value

    @property
    def height(self):
        return f"{self._height}"

    @height.setter
    def height(self, value):
        if not value:
            raise ValueError("Height cannot be empty")
        self._height = value

    @property
    def width(self):
        return f"{self._width}"

    @width.setter
    def width(self, value):
        if not value:
            raise ValueError("Width cannot be empty")
        self._width = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if math.isnan(value):
            raise ValueError("Price must be a number")
        self._price = value

    @property
    def rating(self):
        return f"{self._rating}"

    @rating.setter
    def rating(self, value):
        if not value:
            raise ValueError("Rating cannot be empty")
        self._rating = value
