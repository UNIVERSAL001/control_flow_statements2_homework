def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    x = number%7
    if x==0:
        return "Sunday"
    elif x==1:
        return "Monday"
    elif x==2:
        return "Tuesday"
    elif x==3:
        return "Wednesday"
    elif x==4:
        return "Thursday"
    elif x==5:
        return "Friday"
    elif x==6:
        return "Saturday"
