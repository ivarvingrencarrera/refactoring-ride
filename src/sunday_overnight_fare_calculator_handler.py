from src.fare_calculator_handler import FareCalculatorHandler
from src.segment import Segment


class SundayOvernightFareCalculatorHandler(FareCalculatorHandler):
    FARE = 5

    def __init__(self, next_handler: FareCalculatorHandler | None = None) -> None:
        self.next_handler = next_handler

    def calculate(self, segment: Segment) -> float:
        if segment.is_overnight() and segment.is_sunday():
            return segment.distance * self.FARE
        return self.next_handler.calculate(segment)
