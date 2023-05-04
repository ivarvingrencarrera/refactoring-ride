from typing import Any

from src.normal_fare_calculator import NormalFareCalculator
from src.overnight_fare_calculator import OvernightFareCalculator
from src.peak_time_fare_calculator import PeakTimeFareCalculator
from src.segment import Segment
from src.sunday_fare_calculator import SundayFareCalculator
from src.sunday_overnight_fare_calculator import SundayOvernightFareCalculator


class FareCalculatorFactory:
    @staticmethod
    def create(segment: Segment) -> Any:
        fare_calculator: Any
        if segment.is_peak_time():
            fare_calculator = PeakTimeFareCalculator()
        elif segment.is_overnight() and segment.is_sunday():
            fare_calculator = SundayOvernightFareCalculator()
        elif segment.is_overnight() and not segment.is_sunday():
            fare_calculator = OvernightFareCalculator()
        elif not segment.is_overnight() and segment.is_sunday():
            fare_calculator = SundayFareCalculator()
        elif not segment.is_overnight() and not segment.is_sunday():
            fare_calculator = NormalFareCalculator()
        return fare_calculator
