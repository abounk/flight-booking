from tkinter import CASCADE
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class UserModel(Base):
    """User model, contains information for a user.

    Args:
        id (int): ID of the user.
        firstname (str): User's firstname.
        lastname (str): User's lastname.
        age (int): User's age.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(Text, nullable=False)
    lastname = Column(Text, nullable=False)
    age = Column(Integer, nullable=False)

    flight_booking = relationship(
        "FlightBookingModel", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User (id={self.id!r}, firstname={self.firstname!r}, lastname={self.lastname!r}, age={self.age!r})"
