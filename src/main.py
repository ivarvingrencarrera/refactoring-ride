from datetime import datetime


def is_sunday(date):
    return date.weekday() == 6

def calculate_ride(segments):
    fare = 0
    for segment in segments:
        if segment.get("distance") is not None and segment.get("distance") is not None and isinstance(segment.get("distance"), int) and segment.get("distance") > 0:
            if segment.get("date") is not None and isinstance(segment.get("date"), datetime) :
                overnight = segment.get("date").hour >= 22 or segment.get("date").hour <= 6
                if overnight:
                    if is_sunday(segment.get("date")):
                        fare += segment.get("distance") * 5
                    else:
                        fare += segment.get("distance") * 3.90                        
                else:
                    if is_sunday(segment.get("date")):
                        fare += segment.get("distance") * 2.9
                    else:
                        fare += segment.get("distance") * 2.10
            else:
                # print(d)
                return -2
        else:
            # print(distance)
            return -1
    if fare < 10:
        return 10
    else:
        return fare