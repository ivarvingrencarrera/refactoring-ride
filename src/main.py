from datetime import datetime


def calculate_ride(segments):
    result = 0
    for segment in segments:
        if segment.get("distance") is not None and segment.get("distance") is not None and isinstance(segment.get("distance"), int) and segment.get("distance") > 0:
            if segment.get("date") is not None and isinstance(segment.get("date"), datetime) :
                
                # overnight
                
                if segment.get("date").hour >= 22 or segment.get("date").hour <= 6:
                    
                    # not sunday
                    if segment.get("date").weekday() != 6:
                        result += segment.get("distance") * 3.90
                    
                    # sunday
                    else:
                        result += segment.get("distance") * 5
                else:
                    # sunday
                    if segment.get("date").weekday() == 6:
                        result += segment.get("distance") * 2.9
                    else:
                        result += segment.get("distance") * 2.10
            else:
                # print(d)
                return -2
        else:
            # print(distance)
            return -1

    if result < 10:
        return 10
    else:
        return result