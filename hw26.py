from datetime import datetime, timedelta


def get_date_list(from_date: str, to_date: str) -> list:
    from_date = datetime.strptime(from_date, '%Y-%m-%d')
    to_date = datetime.strptime(to_date, '%Y-%m-%d')
    lst = []
    if from_date <= to_date:
        while from_date <= to_date:
            lst.append(from_date.strftime('%Y-%m-%d'))
            from_date += timedelta(days=1)
    elif from_date >= to_date:
        while from_date >= to_date:
            lst.append(from_date.strftime('%Y-%m-%d'))
            from_date -= timedelta(days=1)
    return lst
