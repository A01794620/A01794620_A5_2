"""
 Module. Compute Sales. Exercise of Programming 2 and Static Analysis 5.2
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

import sys
import os

from pathlib import Path

_parent_dir = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))
from common import SaleItem as SaleItemLine # noqa pylint: disable=wrong-import-position, import-error
from common import ParseType as ParseTypeChecker # noqa pylint: disable=wrong-import-position, import-error
from common import JsonManager as JsonHandler # noqa pylint: disable=wrong-import-position, import-error
from common import FileMaster as FileHandler # noqa pylint: disable=wrong-import-position, import-error
# from common import Setting as Settings # noqa pylint: disable=wrong-import-position, import-error
from common import TimeManager as TimeMng # noqa pylint: disable=wrong-import-position, import-error
from common.PrinterHelper import PrinterHelper # noqa pylint: disable=wrong-import-position, import-error

# Req 1. . The program shall be invoked from a command line.
#        . The program shall receive two files as parameters.
#        . The first file will contain information in a
#          JSON format about
#          a catalogue of prices of products.
#        . The second file will contain a record for all
#          sales in a company.
# Req 2. . The program shall compute the total cost for
#          all sales included in the second JSON archive.
#        . The results shall be print on a screen and on a
#          file named SalesResults.txt.
#        . The total cost should include all items in the
#          sale considering the cost for every item in the
#          first file.
#        . The output must be humanreadable, so make it
#          easy to read for the user.
# Req 3. . The program shall include the mechanism to
#          handle invalid data in the file.
#        . Errors should be displayed in the console and the
#          execution must continue.
# Req 4. . The name of the program shall be computeSales.py
# Req 5. . The minimum format to invoke the program shall be as
#          follows:
#          python computeSales.py priceCatalogue.json salesRecord.json
# Req 6. . The program shall manage files having from hundreds
#          of items to thousands of items.
# Req 7. . The program should include at the end of the execution
#          the time elapsed for the execution and calculus of the data.
#        . This number shall be included in the results file and on
#          the screen.
# Req 8. . Be compliant with PEP8.


def fetch_price(products_, product_title):
    """
    Returns the price of the given product.
    Args:
        products_ (object[]): List of products stored.
        product_title (string): product identifier.

    Returns:
        float: the price of the given product.
    """
    price = 0.0
    for product in products_:
        if product.title == product_title:
            price = product.price
    return price


def data_parser(products_file_path_, sales_file_path_,
                file_source_name_, init_time_):
    """
     Parse the raw material source JSON files.
     Print on screen the results.
     Safe in a file the results.

    Args:
        products_file_path_ (string): Path of the file that
                                      contains the product catalog.
        sales_file_path_ (string): Path of the file that
                                   contains the sales list to be computed.
        file_source_name_ (string): origin file source name.
        init_time_ (float): Initial execution Timestamp.

    Returns:
        boolean: It is a procedure of step by step until
                 print/safe results if the process is aborted
                 then False value is returned.
    """
    products = JsonHandler.JsonManager.json_parser(
                ParseTypeChecker.ParseType.PRODUCT,
                products_file_path_)

    sales = JsonHandler.JsonManager.json_parser(
             ParseTypeChecker.ParseType.SALE_ITEM,
             sales_file_path_)

    parse_integrity = True

    if len(products) <= 0 or len(sales) <= 0:
        parse_integrity = False

    current_sale = -1
    sale_counter = 0.0
    ticket_counter = 0
    great_total = 0.0
    carrier_result = ""

    for sale in sales:
        if current_sale != sale.parent_id:
            ticket_counter = ticket_counter + 1

            if current_sale == -1:
                current_sale = sale.parent_id
                sale.print_header(ticket_counter)
                carrier_result += sale.fetch_header(ticket_counter)
            else:
                current_sale = sale.parent_id
                SaleItemLine.SaleItem.print_footer(sale_counter, False)
                carrier_result += SaleItemLine.SaleItem.fetch_footer(
                                   sale_counter, False)
                sale_counter = 0.0
                sale.print_header(ticket_counter)
                carrier_result += sale.fetch_header(ticket_counter)

        price = fetch_price(products, sale.product)
        sale.unitary_price = price
        sale_counter += sale.total
        great_total += sale.total
        print(sale)
        carrier_result += sale.fetch_item_str()

    if sale_counter > 0.0:
        SaleItemLine.SaleItem.print_footer(sale_counter, False)
        carrier_result += SaleItemLine.SaleItem.fetch_footer(
                          sale_counter, False)
    else:
        pass

    if parse_integrity:
        SaleItemLine.SaleItem.print_footer(great_total, True)
        carrier_result += SaleItemLine.SaleItem.fetch_footer(great_total, True)
    else:
        pass

    execution_time = TimeMng.TimeManager.get_execution_time(
                      init_time_, TimeMng.TimeManager.get_time())
    PrinterHelper.print_time_stamp(execution_time, False)

    carrier_result += f"\nElapsed Execution Time: {execution_time:.4f} seconds"
    FileHandler.FileMaster.write_to_file(file_source_name_, carrier_result)

    execution_time = TimeMng.TimeManager.get_execution_time(
                    init_time_,
                    TimeMng.TimeManager.get_time())

    PrinterHelper.print_time_stamp(execution_time)
    return parse_integrity


if __name__ == '__main__':
    init_time = TimeMng.TimeManager.get_time()
    file_path = os.path.abspath(__file__)
    file_folder = Path(__file__).parent.parent.resolve()

    if len(sys.argv) > 2:
        if len(sys.argv) > 3:
            print("Only the first two arguments are required. " +
                  "Extra arguments will be ignored.")

        product_file_path = sys.argv[1]
        sales_file_path = sys.argv[2]

        file_source_name = sales_file_path.replace(".", "_")

        data_parser(product_file_path, sales_file_path,
                    file_source_name, init_time)
    else:
        PrinterHelper.print_help(file_path, file_folder)
