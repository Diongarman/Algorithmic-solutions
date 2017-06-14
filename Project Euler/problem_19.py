import datetime

start_date = datetime.date(1901, 01,01)
end_date = datetime.date(2000,12,31)

delta = end_date - start_date

sunday_count = 0
for day in range(delta.days+1):
	start_date = start_date + datetime.timedelta(days=1)
	if start_date.weekday() == 6 and start_date.day == 1:
		sunday_count += 1

print sunday_count
