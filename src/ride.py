from datetime import datetime

from src.fare_calculator_factory import FareCalculatorFactory
from src.segment import Segment


class Ride:
    MIN_FARE = 10.0

    def __init__(self) -> None:
        self.segments: list[Segment] = []

    def add_segment(self, distance: float, date: datetime) -> None:
        self.segments.append(Segment(distance, date))

    def calculate_fare(self) -> float:
        fare: float = 0
        for segment in self.segments:
            fare_calculator = FareCalculatorFactory.create(segment)
            fare += fare_calculator.calculate(segment)
        return 10.0 if fare < self.MIN_FARE else fare
