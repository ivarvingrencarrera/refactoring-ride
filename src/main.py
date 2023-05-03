from datetime import datetime


def calculate_ride(segments):
    result = 0
    for mov in segments:
        if mov.get("dist") is not None and mov.get("dist") is not None and isinstance(mov.get("dist"), int) and mov.get("dist") > 0:
            if mov.get("ds") is not None and isinstance(mov.get("ds"), datetime) :
                
                # overnight
                
                if mov.get("ds").hour >= 22 or mov.get("ds").hour <= 6:
                    
                    # not sunday
                    if mov.get("ds").weekday() != 6:
                        result += mov.get("dist") * 3.90
                    
                    # sunday
                    else:
                        result += mov.get("dist") * 5
                else:
                    # sunday
                    if mov.get("ds").weekday() == 6:
                        result += mov.get("dist") * 2.9
                    else:
                        result += mov.get("dist") * 2.10
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