
import unittest
from datetime import datetime

from src.main import calculate_ride


class RideTest(unittest.TestCase):
    def test_must_complete_a_ride_on_a_weekday_at_a_regular_hour(self):
        segments = [{
            'distance': 10, 
            'date': datetime.fromisoformat("2021-03-10T10:00:00")
        }]
        fare = calculate_ride(segments)
        self.assertEqual(fare, 21)

    def test_must_complete_a_ride_on_a_weekday_at_a_overnight_hour(self):
        segments = [{
            'distance': 10, 
            'date': datetime.fromisoformat("2021-03-10T23:00:00")
        }]
        fare = calculate_ride(segments)
        self.assertEqual(fare, 39)

    def test_must_complete_a_ride_on_a_sunday_at_a_regular_hour(self):
        segments = [{
            'distance': 10, 
            'date': datetime.fromisoformat("2021-03-07T10:00:00")
        }]
        fare = calculate_ride(segments)
        self.assertEqual(fare, 29)

    def test_must_complete_a_ride_on_a_sunday_at_a_overnight_hour(self):
        segments = [{
            'distance': 10, 
            'date': datetime.fromisoformat("2021-03-07T23:00:00")
        }]
        fare = calculate_ride(segments)
        self.assertEqual(fare, 50)

    def test_must_return_negative_if_distance_is_invalid(self):
        segments = [{
            'distance': -10, 
            'date': datetime.fromisoformat("2021-03-07T23:00:00")
        }]
        fare = calculate_ride(segments)
        self.assertEqual(fare, -1)

    def test_must_return_negative_if_date_is_invalid(self):
        segments = [{
            'distance': 10, 
            'date': "abc"
        }]
        fare = calculate_ride(segments)
        self.assertEqual(fare, -2)

    def test_must_complete_a_ride_on_a_weekday_at_a_regular_hour(self):
        segments = [{
            'distance': 1, 
            'date': datetime.fromisoformat("2021-03-10T10:00:00")
        }]
        fare = calculate_ride(segments)
        self.assertEqual(fare, 10)
