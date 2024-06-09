def get_string (month_to_get):
    # Instantiate the month_string variable
    month_string = None

    # Check the month to return
    if month_to_get == 1:
        month_string = "januari"
    elif month_to_get == 2:
        month_string = "februari"
    elif month_to_get == 3:
        month_string = "mars"
    elif month_to_get == 4:
        month_string = "april"
    elif month_to_get == 5:
        month_string = "maj"
    elif month_to_get == 6:
        month_string = "juni"
    elif month_to_get == 7:
        month_string = "juli"
    elif month_to_get == 8:
        month_string = "augusti"
    elif month_to_get == 9:
        month_string = "september"
    elif month_to_get == 10:
        month_string = "oktober"
    elif month_to_get == 11:
        month_string = "november"
    elif month_to_get == 12 or month_to_get == 0:
        month_string = "december"
    return month_string

def get_month_num(month):
    month_string = None

    if month == "januari" or month == "jan":
        month_string = 1
    elif month == "februari" or month == "feb":
        month_string = 2
    elif month == "mars" or month == "mar":
        month_string = 3
    elif month == "april" or month == "apr":
        month_string = 4
    elif month == "maj":
        month_string = 5
    elif month == "juni" or month == "jun":
        month_string = 6
    elif month == "juli" or month == "jul":
        month_string = 7
    elif month == "augusti" or month == "aug":
        month_string = 8
    elif month == "september" or month == "sep":
        month_string = 9
    elif month == "oktober" or month == "okt":
        month_string = 10
    elif month == "november" or month == "nov":
        month_string = 11
    elif month == "december" or month == "dec":
        month_string = 12
    return month_string
