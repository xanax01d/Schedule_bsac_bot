from datetime import datetime, timedelta

date = datetime.now()

if date.month >= 8:
    startYear = date.year
else:
    startYear = date.year - 1

firstday = datetime(startYear, 8, 1)

startWeek = None
endWeek = None

thisWeek = None

if firstday.weekday() == 6:
    if date.month == 8 and date.day == 1:
        thisWeek = 1
    else:
        endWeek = firstday.replace(day=1)
        startWeek = firstday.replace(day=-5)
else:
    weekday = firstday.weekday()
    temp = firstday
    startWeek = firstday.replace(day=1-(weekday-1))
    endWeek = temp.replace(day=1+(7-weekday))
    endWeek = endWeek.replace(hour=23, minute=59, second=59, microsecond=999)

if thisWeek is None:
    thisWeek = 1
    if startWeek < date and endWeek > date:
        pass
    else:
        while not(startWeek < date and endWeek > date):
            startWeek = startWeek + timedelta(weeks=1)
            endWeek = endWeek + timedelta(weeks=1)
            endWeek = endWeek.replace(hour=23, minute=59, second=59, microsecond=999)
            if thisWeek != 4:
                thisWeek += 1
            else:
                thisWeek = 1
def return_week():
    return(thisWeek);