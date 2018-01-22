import time
import requests

start_perf = time.perf_counter()
start_time = time.time()

time.sleep(2)
# r = requests.get('http://arstechnica.com')

end_perf = time.perf_counter()
end_time = time.time()

perf = end_perf - start_perf
total = end_time - start_time

print("Perf counter raw: {0}".format(perf))
print("Time counter raw: {0}".format(total))

print("Perf counter ms: {0}".format(int(perf * 1000)))
print("Time counter ms: {0}".format(int(total * 1000)))
