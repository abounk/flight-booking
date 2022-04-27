from sqlalchemy import Column, Integer, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class FlightBooking(Base):
    """FlightBooking model, contian informnation for a flight booking.

    Args:
        id (int): ID of the booking.
        flight_class (str): Class of the flight (eg. First-class, Business, Economy).
        seat_number (str): Seat number.
        user_id (int): ID of the user.
        current (str): Starting country.
        destination (str): Destination country.
        boarding_date (Datetime): datetime of on boarding date.
    """
    __tablename__ = "flight_bookings"

    id = Column(Integer, primary_key=True)
    flight_class = Column(Text, nullable=False)
    seat = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    current = Column(Text, nullable=False)
    destination = Column(Text, nullable=False)
    boarding_date = Column(Text, nullable=False)

    user = relationship("User", back_populates="flight_booking")

    def __repr__(self) -> str:
        return f"FlightBooking (id={self.id}, flight_class={self.flight_class}, seat={self.seat},\
 user_id={self.user_id}, current={self.current}, destination={self.destination}, boarding_date={self.boarding_date})"
