from app_controle_gastos.frontend.central_windows import CentralWindows


class Main:
    @staticmethod
    def run() -> None:
        CentralWindows().tela_inicial()


if __name__ == '__main__':
    Main.run()
