class Setting:

    def __str__(self):
        return self.__class__.__name__

    @property
    def version(self):
        return self.VER

    # GLobal settings to be used across all modules.
    HEAD_SYMBOL= "—"
    SUB_HEAD_SYMBOL= "—"
    OPEN_SYMBOL = "‹"
    CLOSE_SYMBOL = "›"

    VER = "1.0"
    APPLY_TOP = False
    TOP = 4
    RESOURCE_PATH = "tests\\"
    RESULT_PATH = "results\\"
    COL_WIDTH = 60
    OUTPUT_FILE = "SalesResults.txt"
