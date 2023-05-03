from datetime import datetime


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
        if is_valid_distance(segment.get("distance")):
            if is_valid_date(segment.get("date")):
                if is_overnight(segment.get("date")) and is_sunday(segment.get("date")):
                    fare += segment.get("distance") * 5
                elif is_overnight(segment.get("date")) and not is_sunday(segment.get("date")):
                    fare += segment.get("distance") * 3.90           
                elif is_sunday(segment.get("date")) and is_sunday(segment.get("date")):
                    fare += segment.get("distance") * 2.9
                elif is_sunday(segment.get("date")) and not is_sunday(segment.get("date")):   
                    fare += segment.get("distance") * 2.10
            else:
                return -2
        else:
            return -1
    if fare < 10:
        return 10
    else:
        return fare