# tests 5 second results, ONLY for single-threaded programs

from functools import wraps
import errno
import os
import signal
from boost import timing

operationCount = 0
TIMEOUT_ = False

class TimeoutError(Exception):
    if operationCount is not 0:
        TIMEOUT_ = True

def timeout(seconds = 10, error_message = "heh"):
    global operationCount 
    operationCount += 1
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator

# http://stackoverflow.com/questions/2281850/timeout-function-if-it-takes-too-long-to-finish