import unittest
from datetime import datetime

from parameterized import parameterized

from src.ride import Ride


class RideTest(unittest.TestCase):
    def test_must_complete_a_ride_on_a_weekday_at_a_regular_hour(self) -> None:
        ride = Ride()
        ride.add_segment(10.0, datetime.fromisoformat('2021-03-10T10:00:00'))
        fare = ride.calculate_fare()
        self.assertEqual(fare, 21.0)

    def test_must_complete_a_ride_on_a_weekday_at_a_overnight_hour(self) -> None:
        ride = Ride()
        ride.add_segment(10.0, datetime.fromisoformat('2021-03-10T23:00:00'))
        fare = ride.calculate_fare()
        self.assertEqual(fare, 39.0)

    def test_must_complete_a_ride_on_a_sunday_at_a_regular_hour(self) -> None:
        ride = Ride()
        ride.add_segment(10.0, datetime.fromisoformat('2021-03-07T10:00:00'))
        fare = ride.calculate_fare()
        self.assertEqual(fare, 29.0)

    def test_must_complete_a_ride_on_a_sunday_at_a_overnight_hour(self) -> None:
        ride = Ride()
        ride.add_segment(10.0, datetime.fromisoformat('2021-03-07T23:00:00'))
        fare = ride.calculate_fare()
        self.assertEqual(fare, 50.0)

    def test_must_return_minimum_fare(self) -> None:
        ride = Ride()
        ride.add_segment(1.0, datetime.fromisoformat('2021-03-10T10:00:00'))
        fare = ride.calculate_fare()
        self.assertEqual(fare, 10.0)

    @parameterized.expand(
        [
            datetime.fromisoformat('2021-03-10T07:00:00'),
            datetime.fromisoformat('2021-03-10T07:30:00'),
            datetime.fromisoformat('2021-03-10T08:00:00'),
            datetime.fromisoformat('2021-03-10T08:30:00'),
            datetime.fromisoformat('2021-03-10T18:00:00'),
            datetime.fromisoformat('2021-03-10T18:30:00'),
            datetime.fromisoformat('2021-03-10T19:00:00'),
            datetime.fromisoformat('2021-03-10T19:30:00'),
        ]
    )
    def test_must_complete_a_ride_on_a_weekday_at_a_peak_time(self, date: datetime) -> None:
        ride = Ride()
        ride.add_segment(10.0, date)
        fare = ride.calculate_fare()
        self.assertEqual(fare, 60.0)
