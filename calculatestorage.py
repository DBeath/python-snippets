from __future__ import division
import sys

kb = 1024
mb = 1024 ** 2
gb = 1024 ** 3
tb = 1024 ** 4
pb = 1024 ** 5

entrysize = 4281


def print_totals(totalsize):
    print("KB: {:f}".format(totalsize / kb))
    print("MB: {:f}".format(totalsize / mb))
    print("GB: {:f}".format(totalsize / gb))
    print("TB: {:f}".format(totalsize / tb))
    print("PB: {:f}".format(totalsize / pb))
    print()

entries_per_day = int(sys.argv[1])


print("Daily Entries: {:,}".format(entries_per_day))

print()
entries_per_hour = entries_per_day / 24
print('Entries per Hour: {:.0f}'.format(entries_per_hour))
entries_per_minute = entries_per_day / 1440
print('Entries per Minute: {:.2f}'.format(entries_per_minute))
entries_per_second = entries_per_day / 86400
print('Entries per Second: {:.2f}'.format(entries_per_second))
print()


daily_size = entries_per_day * entrysize
print('Daily Bytes: {:,}'.format(daily_size))
print_totals(daily_size)

weekly_entries = entries_per_day * 7
print('Weekly Entries: {:,}'.format(weekly_entries))
weekly_size = weekly_entries * entrysize
print('Weekly Bytes: {:,}'.format(weekly_size))
print_totals(weekly_size)

monthly_entries = int((entries_per_day * 365) / 12)
print('Monthly Entries: {:,}'.format(monthly_entries))
monthly_size = monthly_entries * entrysize
print('Monthly Bytes: {:,}'.format(monthly_size))
print_totals(monthly_size)

yearly_entries = entries_per_day * 365
print('Yearly Entries: {:,}'.format(yearly_entries))
yearly_size = yearly_entries * entrysize
print('Yearly Bytes: {:,}'.format(yearly_size))
print_totals(yearly_size)
