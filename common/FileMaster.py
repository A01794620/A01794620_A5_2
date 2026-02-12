# External Libraries
from pathlib import Path
from colorama import init, Fore
init(autoreset=True)

# Project Common Classes
from common.Setting import Setting
from common.TimeManager import TimeManager
from common.PrinterHelper import PrinterHelper

class FileMaster:

    @staticmethod
    def write_to_file(file_source_name, results_to_print_):
        head_ = Setting.HEAD_SYMBOL * Setting.COL_WIDTH
        results_to_print = head_ + "\n" + results_to_print_ + "\n" + head_ + "\n"

        try:
            file_path_to_write = FileMaster.get_next_file_name_path(file_source_name)
            file_path_to_write.parent.mkdir(parents=True, exist_ok=True)
            file_path_to_write.write_text(results_to_print, encoding="utf-8")
            print("Results stored in:")
            print(f"{Fore.CYAN}'{file_path_to_write}'")
        except FileNotFoundError as e:
            error_to_print = f"FileNotFoundError: {e}"
            PrinterHelper.print_error(error_to_print)

    @staticmethod
    def get_next_file_name_path(file_source_name):
        file_name_to_write = Setting.OUTPUT_FILE
        current_utc_seconds = TimeManager.get_utc()
        current_utc_seconds = str(current_utc_seconds).replace(".", "_")

        plain_filename = (Setting.RESULT_PATH + "\\" + file_source_name +
                          "\\" + current_utc_seconds + "\\" + file_name_to_write)

        return Path(plain_filename)
