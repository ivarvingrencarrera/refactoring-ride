import unittest
from datetime import datetime

from src.segment import Segment


class SegmentTest(unittest.TestCase):
    def test_must_return_negative_if_distance_is_invalid(self) -> None:
        with self.assertRaises(ValueError) as context:
            Segment(-10.0, datetime.fromisoformat('2021-03-07T23:00:00'))
        self.assertEqual(str(context.exception), 'Invalid distance')

    def test_must_return_negative_if_date_is_invalid(self) -> None:
        with self.assertRaises(ValueError) as context:
            Segment(10.0, 'abc')   # type: ignore
        self.assertEqual(str(context.exception), 'Invalid date')
