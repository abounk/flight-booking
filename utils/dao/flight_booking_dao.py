from typing import List, Any
from sqlalchemy.orm.query import Query
from utils.dao.dao_base import Dao
from models.flight_booking import FlightBooking


class FlightBookingDao(Dao):

    def get_all_booking(self) -> List[FlightBooking]:
        """Get all booking form the database.

        Returns:
            List[FlightBooking]: List
        """
        booking_list = self.session.query(FlightBooking).all()
        return booking_list

    def get_booking_by_id(self, id: int) -> FlightBooking:
        """Get a transaction from a specified id.

        Args:
            id (int): Booking ID.

        Returns:
            FlightBookingModel: FlightBooking.
        """
        booking = self.session.query(FlightBooking).filter(
            FlightBooking.id == id).all().pop()
        return booking

    def create_booking(self, booking: FlightBooking) -> None:
        """Insert a booking into the database.

        Args:
            booking (FlightBooking): Instance of FlightBooking.
        """
        self.session.add(booking)
        self.session.commit()
