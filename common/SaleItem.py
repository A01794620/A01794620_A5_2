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
from colorama import init, Fore
from common.Setting import Setting

init(autoreset=True)


# pylint: disable=too-many-instance-attributes
# Disabled R0902: Too many instance attributes
class SaleItem:
    """
    SaleItem. It is a module which holds all features
    linked to the entity Sale Item.
    The Sale Items are the units for every Sale.
    A Sale Item has static characteristics as the
    Sale Date and its unique ID, but also has
    characteristics that are calculations inputs
    such the Quantity and the Product Price;
    which is extracted form the entity Product.
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
        """
        Prepare a valid string for either print in
        screen or write in a file.

        Args:

        Returns:
        string: valid object string representation.
        """

        return (f"•{self.product:<30}\t"
                f"{self.unitary_price:.2f}\t"
                f"{self.quantity:000.0f}\t"
                f"{self.total:,.2f}\t"
                f"{"":>1}"
                "\n")

    def fetch_header(self, page_number=0):
        """
        Prepare a valid Header formated string
        Args:
            page_number (int): the page tab number for reference.
            Returns:
                string: the valid string to be used as header.
        """

        symbol = Setting.HEAD_SYMBOL
        symbol_open = Setting.OPEN_SYMBOL
        symbol_close = Setting.CLOSE_SYMBOL

        break_str = (symbol_open +
                     f"Ticket No.{str(page_number).zfill(4)}" + symbol_close)

        header_str = f"{break_str}\n" \
                     f"\nSale Code: {self._parent_id}\tDate: {self.date}\n"

        header_str += symbol * Setting.COL_WIDTH + "\n"

        header_str += f"{"Product":<30}\t" \
                      f"{"Price"}\t" \
                      f"{"Quant."} " \
                      f"{"Total"}" \
                      f"{"":>1}" \
                      "\n"

        return header_str

    def print_header(self, page_number=0):
        """
        Print a valid header formated string
        Args:
            page_number (int): the page tab number for reference.

        Returns:
              void: this methods print in the end-user screen.
         """
        header_str = self.fetch_header(page_number)
        print(header_str)

    @staticmethod
    def fetch_footer(
            great_total_=0.0,
            is_great_total_=False,
            is_screen_out=True):
        """
         Prepare and return a valid Footer formated string
         Args:
             great_total_ (float): total of the footer.
             is_great_total_ (boolean): flag to check if the total is
             great total or not.
             is_screen_out: it depends if the output is screen then use
             colors, otherwise no.

             Returns:
                 string: the valid strinclear
                 g to be used as header.
         """

        symbol = Setting.HEAD_SYMBOL
        prefix = "Ticket Total:"
        tab_len = 5
        tab = "\t"
        font_color = f"{Fore.LIGHTWHITE_EX}"

        if is_great_total_:
            symbol = "—"
            prefix = "Great Total:"
            font_color = f"{Fore.CYAN}"

        if not is_screen_out:
            font_color = " "

        footer_str = symbol * Setting.COL_WIDTH + "\n"
        footer_str += (f"{font_color}{prefix}{tab_len * tab}" +
                       f"{great_total_:,.2f}\t\n")

        if is_screen_out:
            footer_str += f"{Fore.WHITE}"

        if is_great_total_:
            footer_str += symbol * Setting.COL_WIDTH + "\n"

        return footer_str

    @staticmethod
    def print_footer(great_total_=0.0, is_great_total_=False):
        """
        Print a valid Footer formated string
        Args:
            great_total_ (float): total of the footer.
            is_great_total_ (boolean): flag to check if the total is
            great total or not.

            Returns:
              void: this methods print in the end-user screen.
        """
        footer_str = SaleItem.fetch_footer(great_total_, is_great_total_)
        print(footer_str)

    @property
    def parent_id(self):
        """
        Get or set the sale parent to
        perform sales items groups.
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        if math.isnan(value):
            raise ValueError("Sales Parent ID should be a number")
        self._parent_id = value

    @property
    def date(self):
        """
        Get or set the date of the sale.
        """
        return f"{self._date}"

    @date.setter
    def date(self, value):
        if not value:
            raise ValueError("Date cannot be empty")
        self._date = value

    @property
    def product(self):
        """
        Get or set the product linked to the
        sale item.
        """
        return f"{self._product}"

    @product.setter
    def product(self, value):
        if not value:
            raise ValueError("Product cannot be empty")
        self._product = value

    @property
    def quantity(self):
        """
        Get or set the quantity of products on the sale item.
        """
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if math.isnan(value):
            raise ValueError("Quantity must be a number")
        self._quantity = value

    @property
    def unitary_price(self):
        """
        Get or set the price of the product
        linked to the sale item.
        It might be a numerical value.
        """
        return self._unitary_price

    @unitary_price.setter
    def unitary_price(self, value):
        if math.isnan(value):
            raise ValueError("Unitary Price must be a number")
        self._unitary_price = value

    @property
    def total(self):
        """
        Get the total of the sale item.
        """
        return self._unitary_price * self._quantity
