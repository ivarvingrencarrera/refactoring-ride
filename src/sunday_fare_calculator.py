from src.fare_calculator import FareCalculator
from src.segment import Segment


class SundayFareCalculator(FareCalculator):
    FARE = 2.9

    def calculate(self, segment: Segment) -> float:
        return segment.distance * self.FARE
