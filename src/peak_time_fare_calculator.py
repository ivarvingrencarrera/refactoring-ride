
from src.fare_calculator import FareCalculator
from src.segment import Segment


class PeakTimeFareCalculator(FareCalculator):
    FARE = 6

    def calculate(self, segment: Segment) -> float:
        return segment.distance * self.FARE
