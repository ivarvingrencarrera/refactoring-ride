from datetime import datetime


class Segment:
    SUNDAY_NUMBER = 6
    OVERNIGHT_START_HOUR = 22
    OVERNIGHT_END_HOUR = 6
    MORNING_PEAK_TIME_START_HOUR = 7
    MORNING_PEAK_TIME_END_HOUR = 9
    NIGHT_PEAK_TIME_START_HOUR = 18
    NIGHT_PEAK_TIME_END_HOUR = 20

    def __init__(self, distance: float, date: datetime) -> None:
        if not self.is_valid_distance(distance):
            raise ValueError('Invalid distance')
        if not self.is_valid_date(date):
            raise ValueError('Invalid date')
        self.distance = distance
        self.date = date
        self.hour = date.hour

    def is_valid_distance(self, distance: float) -> bool:
        return distance is not None and isinstance(distance, float) and distance > 0

    def is_valid_date(self, date: datetime) -> bool:
        return date is not None and isinstance(date, datetime)

    def is_sunday(self) -> bool:
        return self.date.weekday() == self.SUNDAY_NUMBER

    def is_overnight(self) -> bool:
        return self.hour >= self.OVERNIGHT_START_HOUR or self.hour <= self.OVERNIGHT_END_HOUR

    def is_peak_time(self) -> bool:
        return (
            self.hour >= self.MORNING_PEAK_TIME_START_HOUR
            and self.hour < self.MORNING_PEAK_TIME_END_HOUR
        ) or (
            self.hour >= self.NIGHT_PEAK_TIME_START_HOUR
            and self.hour < self.NIGHT_PEAK_TIME_END_HOUR
        )
