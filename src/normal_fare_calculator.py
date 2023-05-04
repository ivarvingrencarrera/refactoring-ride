
from src.fare_calculator import FareCalculator
from src.segment import Segment


class NormalFareCalculator(FareCalculator):
    FARE = 2.1

    def calculate(self, segment: Segment) -> float:
        return segment.distance * self.FARE
