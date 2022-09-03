import configparser

class KeysDB(configparser.ConfigParser):
    def __init__(self, tipo_config: str='secret') -> None:
        super().__init__()
        self.read(f'app_controle_gastos/{tipo_config}_config.ini')
        self.USERS = self.get('DB', 'user')
        self.HOST = self.get('DB', 'host')
        self.PASSWORD = self.get('DB', 'passwd')
        self.PORT = self.get('DB', 'port')
        self.DATABASE = self.get('DB', 'database')
