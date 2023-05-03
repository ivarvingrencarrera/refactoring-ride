from datetime import datetime


def calculate_ride(segments):
    result = 0
    for segment in segments:
        if segment.get("dist") is not None and segment.get("dist") is not None and isinstance(segment.get("dist"), int) and segment.get("dist") > 0:
            if segment.get("ds") is not None and isinstance(segment.get("ds"), datetime) :
                
                # overnight
                
                if segment.get("ds").hour >= 22 or segment.get("ds").hour <= 6:
                    
                    # not sunday
                    if segment.get("ds").weekday() != 6:
                        result += segment.get("dist") * 3.90
                    
                    # sunday
                    else:
                        result += segment.get("dist") * 5
                else:
                    # sunday
                    if segment.get("ds").weekday() == 6:
                        result += segment.get("dist") * 2.9
                    else:
                        result += segment.get("dist") * 2.10
            else:
                # print(d)
                return -2
        else:
            # print(dist)
            return -1

    if result < 10:
        return 10
    else:
        return result