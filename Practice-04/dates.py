import datetime
today = datetime.datetime.now() #module.class.method
five_days_ago = today - datetime.timedelta(days=5)  #other class timedelta
print("Five days ago:", five_days_ago)

yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

now_no_microseconds = today.replace(microsecond=0)
print("Current time without microseconds:", now_no_microseconds)

date1 = datetime.datetime(2026, 2, 27, 12, 0, 0)
date2 = datetime.datetime(2026, 2, 26, 8, 30, 0)
diff_seconds = (date1 - date2).total_seconds()
print("Difference in seconds:", diff_seconds)
