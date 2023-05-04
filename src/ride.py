from datetime import datetime

from src.fare_calculator_handler import FareCalculatorHandler
from src.segment import Segment


class Ride:
    MIN_FARE = 10.0

    def __init__(self, fare_calculator_handler: FareCalculatorHandler) -> None:
        self.segments: list[Segment] = []
        self.fare_calculator_handler = fare_calculator_handler

    def add_segment(self, distance: float, date: datetime) -> None:
        self.segments.append(Segment(distance, date))

    def calculate_fare(self) -> float:
        fare: float = sum(
            self.fare_calculator_handler.calculate(segment) for segment in self.segments
        )
        return 10.0 if fare < self.MIN_FARE else fare
