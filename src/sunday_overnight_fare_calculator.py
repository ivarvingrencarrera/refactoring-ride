from src.fare_calculator import FareCalculator
from src.segment import Segment


class SundayOvernightFareCalculator(FareCalculator):
    FARE = 5.0

    def calculate(self, segment: Segment) -> float:
        return segment.distance * self.FARE
