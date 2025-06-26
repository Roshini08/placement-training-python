def validate_date(date_str):
    from datetime import datetime
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False
