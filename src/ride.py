from datetime import datetime

from src.segment import Segment


class Ride:
    SUNDAY_OVERNIGHT_FARE = 5.0
    OVERNIGHT_FARE = 3.9
    SUNDAY_FARE = 2.9
    NORMAL_FARE = 2.1
    MIN_FARE = 10.0

    def __init__(self) -> None:
        self.segments: list[Segment] = []

    def add_segment(self, distance: float, date: datetime) -> None:
        self.segments.append(Segment(distance, date))

    def calculate_fare(self) -> float:
        fare: float = 0
        for segment in self.segments:
            if segment.is_overnight() and segment.is_sunday():
                fare += segment.distance * self.SUNDAY_OVERNIGHT_FARE
            elif segment.is_overnight() and not segment.is_sunday():
                fare += segment.distance * self.OVERNIGHT_FARE
            elif not segment.is_overnight() and segment.is_sunday():
                fare += segment.distance * self.SUNDAY_FARE
            elif not segment.is_overnight() and not segment.is_sunday():
                fare += segment.distance * self.NORMAL_FARE
        return 10.0 if fare < self.MIN_FARE else fare
