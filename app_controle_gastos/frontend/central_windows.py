import sys
from typing import Sequence
from PyQt5.QtWidgets import QApplication

from app_controle_gastos.frontend.tela_inicial import TelaInicial


class CentralWindows(QApplication):
    def __init__(self, args_sys: Sequence[str]=sys.argv) -> None:
        super().__init__(args_sys)
    
    def tela_inicial(self) -> None:
        window = TelaInicial()
        window.show()
        self.exec()
