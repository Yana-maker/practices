from datetime import date


def calculate_age(birthdate):
    today = date.today()

    # Calculate age in years
    age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    # Calculate age in months and days
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age_months = (12 - birthdate.month) + today.month - 1
    else:
        age_months = today.month - birthdate.month

    # Calculate days
    if today.day < birthdate.day:
        # Go back one month to get the correct number of days
        # in the previous month
        month_ago = (today.month - 1) if today.month > 1 else 12
        days_in_month = (date(today.year, today.month, 1) - date(today.year, month_ago, 1)).days
        age_days = days_in_month - (birthdate.day - today.day)
    else:
        age_days = today.day - birthdate.day

    return f'''
{age_years:{'^6'}} - года,
{age_months:{'^6'}} - месяцев,
{age_days:{'^6'}} - дней
    '''


birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
year, month, day = map(int, birthdate_str.split('-'))
birthdate = date(year, month, day)

print(calculate_age(birthdate))
