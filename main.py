from models.flight_booking import FlightBooking
from utils.flight_booking_db import FlightBookingDb

from datetime import datetime, timedelta

flight_booking_db = FlightBookingDb()

print(flight_booking_db.user().get_user_by_id(3))
print(flight_booking_db.booking().get_booking_by_id(3))
print(flight_booking_db.booking().get_all_booking())

onboarding_date = datetime.now() + timedelta(days=1)

date_time_obj = onboarding_date.strftime('%d/%m/%Y %H:%M:%S')

booking = FlightBooking(flight_class="Bussiness", seat_number=111,
                        user_id=11, current="Chiangmai", destination="Bangkok", boarding_date=date_time_obj)

flight_booking_db.booking().create_booking(booking)