from datetime import datetime


class Segment:
    SUNDAY_NUMBER = 6
    OVERNIGHT_START = 22
    OVERNIGHT_END = 6

    def __init__(self, distance: float, date: datetime) -> None:
        if not self.is_valid_distance(distance):
            raise ValueError('Invalid distance')
        if not self.is_valid_date(date):
            raise ValueError('Invalid date')
        self.distance = distance
        self.date = date

    def is_valid_distance(self, distance: float) -> bool:
        return distance is not None and isinstance(distance, float) and distance > 0

    def is_valid_date(self, date: datetime) -> bool:
        return date is not None and isinstance(date, datetime)

    def is_sunday(self) -> bool:
        return self.date.weekday() == self.SUNDAY_NUMBER

    def is_overnight(self) -> bool:
        return self.date.hour >= self.OVERNIGHT_START or self.date.hour <= self.OVERNIGHT_END
