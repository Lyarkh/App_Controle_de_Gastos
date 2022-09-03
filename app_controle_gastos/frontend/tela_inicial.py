import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from typing import Sequence

class CentralWindows(QApplication):
    def __init__(self, args_sys: Sequence[str]=sys.argv) -> None:
        super().__init__(args_sys)
    
    def tela_inicial(self) -> None:
        window = TelaInicial()
        window.show()
        self.exec()

    def teste(self):
        print('Error')
        
class TelaInicial(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(r"app_controle_gastos\frontend\layouts\tela_inicial.ui", self)


CentralWindows().tela_inicial()
