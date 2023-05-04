import unittest
from datetime import datetime

from parameterized import parameterized

from src.ride import Ride


class RideTest(unittest.TestCase):
    def setUp(self) -> None:
        self.ride = Ride()

    def base_function_test(self, arg0: float, arg1: str, arg2: float) -> None:
        self.ride.add_segment(arg0, datetime.fromisoformat(arg1))
        fare = self.ride.calculate_fare()
        self.assertEqual(fare, arg2)

    def test_must_complete_a_ride_on_a_weekday_at_a_normal_time(self) -> None:
        self.base_function_test(10.0, '2021-03-10T10:00:00', 21)

    def test_must_complete_a_ride_on_a_weekday_at_a_overnight_time(self) -> None:
        self.base_function_test(10.0, '2021-03-10T23:00:00', 39.0)

    def test_must_complete_a_ride_on_a_sunday_at_a_normal_time(self) -> None:
        self.base_function_test(10.0, '2021-03-07T10:00:00', 29.0)

    def test_must_complete_a_ride_on_a_sunday_at_a_overnight_time(self) -> None:
        self.base_function_test(10.0, '2021-03-07T23:00:00', 50.0)

    @parameterized.expand(
        [
            '2021-03-10T07:00:00',
            '2021-03-10T08:59:00',
            '2021-03-10T18:00:00',
            '2021-03-10T19:59:59',
        ]
    )
    def test_must_complete_a_ride_on_a_weekday_at_a_peak_time(self, date: str) -> None:
        self.base_function_test(10.0, date, 60.0)

    def test_must_return_minimum_fare(self) -> None:
        self.base_function_test(1.0, '2021-03-10T10:00:00', 10.0)
