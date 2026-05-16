from datetime import datetime
current_date = datetime.now().date()  #todays date initialized as current date
date_list = [datetime.strptime(date, '%Y-%m-%d').date() for date in ['2027-01-01', '2025-06-01', '2026-06-30', '2026-03-31']]
def filter_date(date):
    return date >= current_date
future_date = list(filter(filter_date, date_list))
filter_dates = [date.strftime('%Y-%B-%d') for date in future_date] #string value of month
#filter_dates = [date.strftime('%Y-%m-%d') for date in future_date]  #numerical value of month
print(filter_dates)
