from datetime import datetime, timedelta

def get_day_as_string (year, month, day):
    # Calculate the date for the specific day in the previous month
    first_day_of_month = datetime(year, month, 1)
    specific_day = first_day_of_month + timedelta(days=day - 1)

    # Format the date to get the day of the week as a string
    day_of_week = specific_day.strftime('%A').lower()

    swedish_day = None
    # Check the month to return
    if day_of_week == "monday":
        swedish_day = "måndag"
    elif day_of_week == "tuesday":
        swedish_day = "tisdag"
    elif day_of_week == "wednesday":
        swedish_day = "onsdag"
    elif day_of_week == "thursday":
        swedish_day = "torsdag"
    elif day_of_week == "friday":
        swedish_day = "fredag"
    elif day_of_week == "saturday":
        swedish_day = "lördag"
    elif day_of_week == "sunday":
        swedish_day = "söndag"
    return(swedish_day)
