from src.fare_calculator_handler import FareCalculatorHandler
from src.segment import Segment


class PeakTimeFareCalculatorHandler(FareCalculatorHandler):
    FARE = 6

    def __init__(self, next_handler: FareCalculatorHandler | None = None) -> None:
        self.next_handler = next_handler

    def calculate(self, segment: Segment) -> float:
        if segment.is_peak_time():
            return segment.distance * self.FARE
        return self.next_handler.calculate(segment)
