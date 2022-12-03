import datetime
current_date = datetime.datetime.now()
new_date = current_date+datetime.timedelta(days=15).date
print(new_date.date())
