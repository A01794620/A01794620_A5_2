from pathlib import Path
from colorama import init, Fore
init(autoreset=True)

from common import SaleItem as SaleItemLine
from common.Setting import Setting as Settings
from common.PrinterHelper import PrinterHelper as Printer
from common import ParseType as ParseTypeChecker
from common import Product as ProductItem

import json

class JsonManager:

    @staticmethod
    def load_from_file(file_path, file_folder):
        data = ""
        error_to_print = ""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:

            error_to_print = f"File was not found:= {file_path}."

            error_to_print = error_to_print + (f"{Fore.RED} \nRemember that the file might be located in" +
                                                        " the following path to be read by the " +
                                                        "program:\n" + f"{Fore.MAGENTA}{file_folder}\\" +
                                                        Settings.RESOURCE_PATH + " <--\n"
                                               f"{Fore.RED}")
            Printer.print_error(error_to_print)

            return data
        except json.JSONDecodeError:

            error_to_print = f"{Fore.RED} Error: Could not decode JSON from the file. Check for valid JSON syntax."
            Printer.print_error(error_to_print)

            return data

    @staticmethod
    def json_parser(parser_type, primitive_json_path):
        obj_container = []
        file_folder = Path(__file__).parent.parent.resolve()

        primitive_json = JsonManager.load_from_file(Settings.RESOURCE_PATH + primitive_json_path, file_folder)

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