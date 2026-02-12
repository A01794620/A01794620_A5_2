from pathlib import Path

class FileMaster:

    @staticmethod
    def write_to_file(results_to_print_):
        try:
            file_path_to_write = Path("results/results.txt")
            file_path_to_write.parent.mkdir(parents=True, exist_ok=True)
            file_path_to_write.write_text(results_to_print_, encoding="utf-8")
        except FileNotFoundError as e:
            error_to_print = f"FileNotFoundError: {e}"