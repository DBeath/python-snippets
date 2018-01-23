import re
import os
import statistics
from pprint import pprint

capture = re.compile('POST "\/push\/(?:[A-Za-z0-9])*" (?:\d{3}) OK in (\d+)ms for')

directory = "/home/dbeath/Documents/Auctorial-Logs"

content = []

for filename in os.listdir(directory):
    if filename.startswith("auctorial"):
        filepath = os.path.join(directory, filename)
        with open(filepath) as f:
            lines = f.readlines()
            content.extend(lines)

# filename = 'auctorial_papertrail_logs'

# with open(filename) as f:
#     content = f.readlines()

print("Found {0} lines".format(len(content)))

times = []

for line in content:
    match = capture.search(line)
    if match:
        if match.group(1):
            times.append(int(match.group(1)))

length = len(times)
print("Found {0} POST times".format(length))

mean = statistics.mean(times)
print('Mean time: {:.0f}ms'.format(mean))

mode = statistics.mode(times)
print("Mode time: {0}ms".format(mode))

median = statistics.median(times)
print('Median time: {:.0f}ms'.format(median))

print("Slowest time: {0}ms".format(max(times)))
print("Fastest time: {0}ms".format(min(times)))
