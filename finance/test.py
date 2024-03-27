from datetime import datetime, date, time, timezone
dt = datetime.now()
format_day = f"{dt.year}-{dt.month}-{dt.day}"
format_time= f"{dt.hour}:{dt.minute}:{dt.second}"

print(format_time)
