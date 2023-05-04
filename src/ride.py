from datetime import datetime
from src.normal_fare_calculator import NormalFareCalculator
from src.overnight_fare_calculator import OvernightFareCalculator
from src.peak_time_fare_calculator import PeakTimeFareCalculator

from src.segment import Segment
from src.sunday_fare_calculator import SundayFareCalculator
from src.sunday_overnight_fare_calculator import SundayOvernightFareCalculator


class Ride:
    MIN_FARE = 10.0

    def __init__(self) -> None:
        self.segments: list[Segment] = []

    def add_segment(self, distance: float, date: datetime) -> None:
        self.segments.append(Segment(distance, date))

    def calculate_fare(self) -> float:
        fare: float = 0
        for segment in self.segments:
            if segment.is_peak_time():
                fare_calculator = PeakTimeFareCalculator()
                fare += fare_calculator.calculate(segment)
            elif segment.is_overnight() and segment.is_sunday():
                fare_calculator = SundayOvernightFareCalculator()
                fare += fare_calculator.calculate(segment)
            elif segment.is_overnight() and not segment.is_sunday():
                fare_calculator = OvernightFareCalculator()
                fare += fare_calculator.calculate(segment)
            elif not segment.is_overnight() and segment.is_sunday():
                fare_calculator = SundayFareCalculator()
                fare += fare_calculator.calculate(segment)
            elif not segment.is_overnight() and not segment.is_sunday():
                fare_calculator = NormalFareCalculator()
                fare += fare_calculator.calculate(segment)
        return 10.0 if fare < self.MIN_FARE else fare
