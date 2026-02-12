"""
 Module. Sale Item. Exercise of Programming 2 and Static Analysis 5.2
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

class SaleItem:

    """
    SaleItem. It is a module which holds all features linked to the entity Sale Item.
    The Sale Items are the units for every Sale.
    A Sale Item has static characteristics as the Sale Date and its unique ID, but also
    has characteristics that are calculations inputs such the Quantity and the Product
    Price; which is extracted form the entity Product.
    """

    def __init__(self, dict_line):
        self.parent_id = int(dict_line['SALE_ID'])
        self.date = str(dict_line['SALE_Date'])
        self.product = str(dict_line['Product'])
        self.quantity = float(dict_line['Quantity'])
        self.unitary_price = 0.0

    def __str__(self):
        return self.fetch_item_str()

    def fetch_item_str(self):
        return (f"•{self.product:<30}\t"
                f"{self.unitary_price:.2f}\t"
                f"{self.quantity:000.0f}\t"
                f"{self.total:,.2f}\t"
                f"{"":>1}"
                "\n")

    def fetch_header(self, page_number=0):
        symbol = "—"
        symbol_open = "‹"
        symbol_close = "›"
        break_str = symbol_open + f"Ticket No.{str(page_number).zfill(4)}" + symbol_close

        header_str = f"{break_str}\n" \
                     f"\nSale Code: {self._parent_id}\tDate: {self.date}\n"

        header_str += symbol * 70 + "\n"

        header_str += f"{"Product":<30}\t" \
                      f"{"Price"}\t" \
                      f"{"Quant."} " \
                      f"{"Total"}" \
                      f"{"":>1}" \
                      "\n"

        return header_str


    def print_header(self, page_number=0):
        header_str = self.fetch_header(page_number)
        print(header_str)

    @staticmethod
    def fetch_footer(great_total_=0.0, is_great_total_=False):
        symbol = "—"
        prefix = ""

        if is_great_total_:
            symbol = "—"
            prefix = "Great "

        footer_str = symbol * 70 + "\n"
        footer_str += f"{prefix}Total:\t\t\t\t\t\t{great_total_:,.2f}\t\n"

        if is_great_total_:
            footer_str += symbol * 70 + "\n"

        return footer_str

    @staticmethod
    def print_footer(great_total_=0.0, is_great_total_=False):
        footer_str = SaleItem.fetch_footer(great_total_, is_great_total_)
        print(footer_str)

    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        if math.isnan(value):
            raise ValueError("Sales Parent ID should be a number")
        self._parent_id = value

    @property
    def date(self):
        return f"{self._date}"

    @date.setter
    def date(self, value):
        if not value:
            raise ValueError("Date cannot be empty")
        self._date = value

    @property
    def product(self):
        return f"{self._product}"

    @product.setter
    def product(self, value):
        if not value:
            raise ValueError("Product cannot be empty")
        self._product = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if math.isnan(value):
            raise ValueError("Quantity must be a number")

        if value < 0:
            print(f"Quantity must be positive: {self.product } {str(value)}")
            #print(f"Quantity cannot be negative")
            #print(f"{self.product } {str(self.quantity)}")

        #print(f"::: Quantity :::{value}")

        self._quantity = value

    @property
    def unitary_price(self):
        return self._unitary_price

    @unitary_price.setter
    def unitary_price(self, value):
        if math.isnan(value):
             raise ValueError("Unitary Price must be a number")
        self._unitary_price= value

    @property
    def total(self):
        return self._unitary_price * self._quantity
