from threading import Thread
from time import sleep, time_ns

class ServerThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.alive = True
        self.last_loop_time = 0

    def run(self):
        while self.alive:
            before_ts = time_ns()
            for num in range(0, 1000):
                pass
            after_ts = time_ns()
            self.last_loop_time = after_ts - before_ts

print('starting up')
thread = ServerThread()

try:
    thread.start()
    while True:
        sleep(1)
except KeyboardInterrupt:
    print('shutting down')
    thread.alive = False
    thread.join()
    last = thread.last_loop_time
    print('loop time in \n' \
          'nanoseconds: ' + str(last) + '\n' + \
          'microseconds: ' + str(last / 1000) + '\n' + \
          'milliseconds: ' + str((last / 1000) / 1000))
