from time import time_ns

before_ts = time_ns()
for num in range(0, 1000):
    pass
after_ts = time_ns()

diff = after_ts - before_ts
print('loop time in \n' \
      'nanoseconds: ' + str(diff) + '\n' + \
      'microseconds: ' + str(diff / 1000) + '\n' + \
      'milliseconds: ' + str((diff / 1000) / 1000))
