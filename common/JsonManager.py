"""
 Module. JSON Manager. Exercise of Programming 2 and Static Analysis 5.2
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

from pathlib import Path
import json
from colorama import init, Fore
init(autoreset=True)


from common import SaleItem as SaleItemLine # noqa pylint: disable=wrong-import-position, import-error
from common.Setting import Setting as Settings # noqa pylint: disable=wrong-import-position, import-error
from common.PrinterHelper import PrinterHelper as Printer # noqa pylint: disable=wrong-import-position, import-error
from common import ParseType as ParseTypeChecker # noqa pylint: disable=wrong-import-position, import-error
from common import Product as ProductItem # noqa pylint: disable=wrong-import-position, import-error


class JsonManager:

    """
    JSON Manager. Is a Class that handles all details about parsing the JSON
    external files which are the raw material of all the system functions.
    """

    @staticmethod
    def load_from_file(file_path, file_folder):
        """
        Read the context of a plain JSON file.

        Args:
            file_path (strig): File path to be read.
            file_folder (Path): Path to the folder where the file is located.
        Returns:
            string[]: The content of the file in lines separation.
        """

        data = ""
        err_to_print = ""
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:

            err_to_print = f"File was not found:= {file_path}."

            err_to_print += (f"{Fore.RED}" +
                             "\nRemember that the file might be located in " +
                             "the following path to be read by the " +
                             "program:\n" + f"{Fore.MAGENTA}{file_folder}\\" +
                             Settings.RESOURCE_PATH + " <--\n"
                             f"{Fore.RED}")

            Printer.print_error(err_to_print)

            return data
        except json.JSONDecodeError:

            err_to_print = (f"{Fore.RED}" +
                            "Error: Could not decode JSON from the file. " +
                            "Check for valid JSON syntax.")
            Printer.print_error(err_to_print)

            return data

    @staticmethod
    def json_parser(parser_type, primitive_json_path):
        """
        Parse the context of a plain JSON file.

        Args:
            parser_type (Literal): The type of object which will work.
            primitive_json_path (string): Path to the folder where
             the file is located.
        Returns:
            object[]: Each item is an object type
            (either Sale Item or Product Item).
        """

        obj_container = []
        file_folder = Path(__file__).parent.parent.resolve()

        primitive_json = JsonManager.load_from_file(
                            Settings.RESOURCE_PATH +
                            primitive_json_path, file_folder)

        for json_line in primitive_json:
            obj_line = None

            if parser_type == ParseTypeChecker.ParseType.PRODUCT:
                obj_line = ProductItem.Product(json_line)
            elif parser_type == ParseTypeChecker.ParseType.SALE_ITEM:
                obj_line = SaleItemLine.SaleItem(json_line)
            else:
                pass
            obj_container.append(obj_line)
        return obj_container
