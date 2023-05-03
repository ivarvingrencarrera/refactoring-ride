import unittest
from datetime import datetime

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
