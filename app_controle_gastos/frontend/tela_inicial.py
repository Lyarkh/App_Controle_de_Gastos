import sys
from PyQt5 import uic
from typing import Sequence
from PyQt5.QtWidgets import QApplication, QWidget

class CentralWindows(QApplication):
    def __init__(self, args_sys: Sequence[str]=sys.argv) -> None:
        super().__init__(args_sys)
    
    def tela_inicial(self) -> None:
        window = TelaInicial()
        window.show()
        self.exec()

        
class TelaInicial(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(r"app_controle_gastos\frontend\layouts\tela_inicial.ui", self)


CentralWindows().tela_inicial()
