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
        """Get a booking from a specified id.

        Args:
            id (int): Booking ID.

        Returns:
            FlightBookingModel: FlightBooking.
        """
        booking = self.session.query(FlightBooking).filter(
            FlightBooking.id == id).all().pop()
        return booking

    def get_booking_by_user_id(self, user_id: int) -> List[FlightBooking]:
        """Get a list of flight bookings by user's id.

        Args:
            user_id (int): id of an user.

        Returns:
            List[FlightBooking]: All bookings of a specified user.
        """
        booking_list = self.session.query(FlightBooking).filter(
            FlightBooking.user_id == user_id).all()
        return booking_list

    def get_booking_by_sorted_date(self) -> List[FlightBooking]:
        """Get bookings that sorted by onboarding date.

        Returns:
            List[FlightBooking]: sorted list of FlightBooking obj.
        """
        booking_list = self.get_all_booking()
        booking_by_date_list = sorted(
            booking_list, key=lambda booking: booking.boarding_date)
        return booking_by_date_list

    def create_booking(self, booking: FlightBooking) -> None:
        """Insert a booking into the database.

        Args:
            booking (FlightBooking): Instance of FlightBooking.
        """
        self.session.add(booking)
        self.session.commit()

    def update_booking(self, id: int, value) -> None:
        """Update a booking in the database

        Args:
            id (int): Booking ID.
            value (Dict): {column_name: new_value}.
        """
        booking = self.session.query(
            FlightBooking).filter(FlightBooking.id == id)
        booking.update(values=value)

        self.session.commit()
