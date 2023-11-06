import datetime

def convert_date(date_string, target_format='%Y-%m-%d'):
    try:
        # Check for format %Y%m%d
        date_object = datetime.datetime.strptime(date_string, '%Y%m%d')
    except ValueError:
        # Check for format %d%m%Y
        try:
            date_object = datetime.datetime.strptime(date_string, '%d%m%Y')
        except ValueError:
            # Check for format %m%d%Y
            try:
                date_object = datetime.datetime.strptime(date_string, '%m%d%Y')
            except ValueError:
                # Invalid date format
                return None

    # Convert to the target format
    converted_date = date_object.strftime(target_format)
    return converted_date

date_strings = ['20150922', '30041998', '12312022']
converted_dates = [convert_date(date_string) for date_string in date_strings]

print(date_strings)
print(converted_dates)
