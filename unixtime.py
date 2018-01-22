from datetime import datetime
import time

dt = datetime.utcnow()
print(dt)
unix_dt = dt.strftime('%s')
print(unix_dt)
print(type(unix_dt))

unix_dt_2 = time.mktime(dt.timetuple())
print unix_dt_2

f = datetime.utcfromtimestamp(float(unix_dt))
print(f)

f_unix = time.mktime(f.timetuple())
print(f_unix)

print

first = datetime(2015, 12, 01, tzinfo=None)
print(first)
unix_first = time.mktime(first.timetuple())
print(unix_first)
