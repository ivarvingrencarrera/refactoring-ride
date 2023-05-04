
from src.fare_calculator import FareCalculator
from src.segment import Segment


class OvernightFareCalculator(FareCalculator):
    FARE = 3.9

    def calculate(self, segment: Segment) -> float:
        return segment.distance * self.FARE
