from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.dao.flight_booking_dao import FlightBookingDao
from utils.dao.user_dao import UserDao


class FlightBookingDb:

    def __init__(self, connection_string: str = "sqlite:///flight.db") -> None:
        db_engine = create_engine(connection_string)
        self.__db_session = sessionmaker(bind=db_engine)()

    def user(self):
        return UserDao(self.__db_session)

    def booking(self):
        return FlightBookingDao(self.__db_session)
