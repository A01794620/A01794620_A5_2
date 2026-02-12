"""
 Module. FileMaster. Exercise of Programming 2 and Static Analysis 5.2
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


# External Libraries
from pathlib import Path
from colorama import init, Fore
init(autoreset=True)

# Project Common Classes
from common.Setting import Setting # noqa pylint: disable=wrong-import-position, import-error
from common.TimeManager import TimeManager # noqa pylint: disable=wrong-import-position, import-error
from common.PrinterHelper import PrinterHelper # noqa pylint: disable=wrong-import-position, import-error


class FileMaster:

    """
    FileMaster. Is a Class that handles all details about files procedures.
    """

    @staticmethod
    def write_to_file(file_source_name, results_to_print_):
        """
        Writes data in a specific file in the local system.

            Args:
                file_source_name (string): Original file name reference.
                results_to_print_ (string): text to be saved in the file
                of the local system.

            Returns:
                void (void): Write the data in the file with no return.
        """
        head_ = Setting.HEAD_SYMBOL * Setting.COL_WIDTH
        results_to_print = (head_ + "\n" + results_to_print_ +
                            "\n" + head_ + "\n")

        try:
            path_write = FileMaster.get_next_file_name_path(file_source_name)
            path_write.parent.mkdir(parents=True, exist_ok=True)
            path_write.write_text(results_to_print, encoding="utf-8")
            print("Results stored in:")
            print(f"{Fore.CYAN}'{path_write}'")
        except FileNotFoundError as e:
            error_to_print = f"FileNotFoundError: {e}"
            PrinterHelper.print_error(error_to_print)

    @staticmethod
    def get_next_file_name_path(file_source_name):
        """
        Calculates the next valid file path to be saved.

            Args:
                file_source_name (sting): The file origin for reference
                usage to create a new folder.

            Returns:
                next valid path (string): It is a new folder/file to be
                                          created on the local system.
        """
        file_name_to_write = Setting.OUTPUT_FILE
        current_utc_seconds = TimeManager.get_utc()
        current_utc_seconds = str(current_utc_seconds).replace(".", "_")

        plain_filename = (Setting.RESULT_PATH + "\\" + file_source_name +
                          "\\" + current_utc_seconds + "\\" +
                          file_name_to_write)

        return Path(plain_filename)
