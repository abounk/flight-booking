from abc import ABC
from sqlalchemy.orm.session import Session


class Dao(ABC):
    def __init__(self, session: Session) -> None:
        """Dao abstract class for dao classes.
        Args:
            session (session): The Connection object of the database.
        """
        self.__session = session

    @property
    def session(self):
        return self.__session
