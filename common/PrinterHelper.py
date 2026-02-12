from colorama import init, Fore
from common.Setting import Setting

init(autoreset=True)

class PrinterHelper:

    @staticmethod
    def print_error(error_str):
        head_ = Setting.HEAD_SYMBOL * Setting.COL_WIDTH

        results_to_print = "\n" + head_ + "\n" + error_str + "\n" + head_ + "\n"
        print(f"{Fore.RED}The following errors were found in the system execution:"
              f"\n{results_to_print}")

    @staticmethod
    def print_help(file_path, file_folder):

        head_ = Setting.HEAD_SYMBOL * Setting.COL_WIDTH

        results_to_print = f"{Fore.RED}\n{head_}\n" \
                           f"This program requires two parameters indicating:\n\n" \
                           f"\ti.The file path to be read and used as Product List Catalog.\n" \
                           f"\tii.The file path to be read and used as a Sales List.\n" \
                           f"\nAdditional parameters will be ignored.\n" \
                           f"\nInvocation example:\n  python '{file_path}' ProductList.json TC1.Sales.json\n" \
                           f"Where the JSON files might be placed in folder:"

        print(f"{Fore.RED}{results_to_print}")
        results_to_print = f"{file_folder}\\{Setting.RESOURCE_PATH} {Setting.OPEN_SYMBOL}{Setting.OPEN_SYMBOL}"
        print(f"{Fore.MAGENTA}{results_to_print}")
        results_to_print = f"{head_}\n"
        print(f"{Fore.RED}{results_to_print}")