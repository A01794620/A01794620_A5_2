"""
 Module. Print Helper. Exercise of Programming 2 and Static Analysis 5.2
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


from colorama import init, Fore
from common.Setting import Setting

init(autoreset=True)


class PrinterHelper:

    """
    Print Helper to handle any message to be displayed on main end-user screen.
    """

    @staticmethod
    def print_error(error_str):
        """
        Print messages under error or exception fashion.

        Args:
            error_str (string): Original error text to print.

        Returns:
           void: System print by console.
        """
        head_ = Setting.HEAD_SYMBOL * Setting.COL_WIDTH

        results_to_print = ("\n" + head_ + "\n" +
                            error_str + "\n" + head_ + "\n")

        print(f"{Fore.RED}The following errors were "
              f"found in the system execution:"
              f"\n{results_to_print}")

    @staticmethod
    def print_help(file_path, file_folder):
        """
        Print help instructions to help the user on the right program usage.

        Args:
            file_path (string): Path to the original file on run.
            file_folder (Path): Path to the folder where the file is located.
        Returns:
            void: System print by console.
        """

        head_ = Setting.HEAD_SYMBOL * Setting.COL_WIDTH

        res_print = f"{Fore.RED}\n{head_}\n" \
                    f"This program requires two parameters indicating:\n\n" \
                    f"\ti.The file path to be read and used as " \
                    f"Product List Catalog.\n" \
                    f"\tii.The file path to be read and used as a " \
                    f"Sales List.\n" \
                    f"\nAdditional parameters will be ignored.\n" \
                    f"\nInvocation example:\n" \
                    f"  python '{file_path}' ProductList.json" \
                    f" TC1.Sales.json\n" \
                    f"Where the JSON files might be placed in folder:"

        print(f"{Fore.RED}{res_print}")

        res_print = (f"{file_folder}\\{Setting.RESOURCE_PATH} " +
                     f"{Setting.OPEN_SYMBOL}{Setting.OPEN_SYMBOL}")

        print(f"{Fore.MAGENTA}{res_print}")
        res_print = f"{head_}\n"
        print(f"{Fore.RED}{res_print}")

    @staticmethod
    def print_time_stamp(execution_time, is_final_time_=True):
        """
        Print the execution time in the very last moment,
        after file is stored and results on screen.
        This elapsed time is wide bigger than the calculation time
        in the local machine.

            Args:
                execution_time (float): Execution time registered.
                is_final_time_ (bool): Flag to either display final time
                or execution time.
            Returns:
                void: System print by console.
        """

        if is_final_time_:
            print(f"{Fore.LIGHTWHITE_EX}Elapsed Time after saving " +
                  "file and listing on screen: " +
                  f"{execution_time: .4f} seconds\n")
        else:
            print(f"{Fore.CYAN}Elapsed Execution Time: " +
                  f"{execution_time: .4f} seconds\n")
