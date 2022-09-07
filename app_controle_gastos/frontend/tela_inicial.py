from PyQt5 import uic
from PyQt5.QtWidgets import  QWidget


class TelaInicial(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("app_controle_gastos/frontend/layouts/tela_inicial.ui", self)
