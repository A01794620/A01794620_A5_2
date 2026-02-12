"""
 Module. Setting. Exercise of Programming 2 and Static Analysis 5.2
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


class Setting:

    """
    Settings to handle global constants across modules.
    """

    def __str__(self):
        return self.__class__.__name__

    @property
    def version(self):
        """
        Get the settings version.
        """
        return self.VER

    # GLobal settings to be used
    # across all modules.
    HEAD_SYMBOL = "—"
    SUB_HEAD_SYMBOL = "—"
    OPEN_SYMBOL = "‹"
    CLOSE_SYMBOL = "›"
    VER = "1.0"
    APPLY_TOP = False
    TOP = 4
    RESOURCE_PATH = "tests\\"
    RESULT_PATH = "results\\"
    COL_WIDTH = 60
    OUTPUT_FILE = "SalesResults.txt"
