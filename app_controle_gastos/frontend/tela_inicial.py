import sys
from PyQt5 import uic
from typing import Sequence
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

from app_controle_gastos.backend.DB.connection import RegistroDB
from app_controle_gastos.backend.DB.schemas import Pessoa


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
        uic.loadUi("app_controle_gastos/frontend/layouts/tela_inicial.ui", self)
