from src.fare_calculator_handler import FareCalculatorHandler
from src.segment import Segment


class OvernightFareCalculatorHandler(FareCalculatorHandler):
    FARE = 3.9

    def __init__(self, next_handler: FareCalculatorHandler | None = None) -> None:
        self.next_handler = next_handler

    def calculate(self, segment: Segment) -> float:
        if segment.is_overnight() and not segment.is_sunday():
            return segment.distance * self.FARE
        if not self.next_handler:
            raise ValueError('')
        return self.next_handler.calculate(segment)
