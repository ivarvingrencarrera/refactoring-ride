from datetime import datetime

SUNDAY_OVERNIGHT_FARE = 5
OVERNIGHT_FARE = 3.9
SUNDAY_FARE = 2.9
NORMAL_FARE = 2.1
MIN_FARE = 10

def is_sunday(date):
    return date.weekday() == 6

def is_overnight(date):
    return date.hour >= 22 or date.hour <= 6

def is_valid_distance(distance):
    return distance is not None and isinstance(distance, int) and distance > 0

def is_valid_date(date):
    return date is not None and isinstance(date, datetime) 

def calculate_ride(segments):
    fare = 0
    for segment in segments:
        if not is_valid_distance(segment.get("distance")): raise ValueError('Invalid distance')
        if not is_valid_date(segment.get("date")): raise ValueError('Invalid date')
        if is_overnight(segment.get("date")) and is_sunday(segment.get("date")):
            fare += segment.get("distance") * SUNDAY_OVERNIGHT_FARE
        elif is_overnight(segment.get("date")) and not is_sunday(segment.get("date")):
            fare += segment.get("distance") * OVERNIGHT_FARE         
        elif is_sunday(segment.get("date")) and is_sunday(segment.get("date")):
            fare += segment.get("distance") * SUNDAY_FARE
        elif is_sunday(segment.get("date")) and not is_sunday(segment.get("date")):   
            fare += segment.get("distance") * NORMAL_FARE
    return 10 if fare < MIN_FARE else fare