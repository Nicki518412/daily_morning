from datetime import datetime, date


def get_count(start_date):
    today = datetime.now()
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


def get_birthday(birthday):
    today = datetime.now()
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days
