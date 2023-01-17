from typing import Tuple, Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app_controle_gastos.tokens.database import KeysDB


class RegistroDB:
    @staticmethod
    def get_connection() -> Tuple[Any, Any]:
        keys = KeysDB()
        engine = create_engine(
            f"mysql://{keys.USER}:{keys.PASSWORD}"
            f"@{keys.HOST}:{keys.PORT}/{keys.DATABASE}",
            echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()

        return session, engine
