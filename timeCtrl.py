"""timeCtrl.py -- some tools related time control
"""

import functools
import time

def timeit(func):
    """This is a decorator using for calculating how much time a method costs"""

    @functools.wraps(func)
    def wrapper(*arg, **kw):
        start_time = time.time()
        ret = func(*arg, **kw)
        end_time = time.time()
        print "{name} costs {seconds}s.".format(name=func.__name__, seconds=end_time-start_time)
        return ret
    return wrapper


class TimeoutError(Exception):
    pass


def timeout(seconds, error_message="Time out."):
    """Set-timeout-tool. But it only can be used in *nix os because signal module needed.
       Multi-thread doesn't work either.
    """
    import signal
    def decorator(func):

        def __timiout_handler(signum, frame):
            raise TimeoutError(error_message)

        @functools.wraps(func)
        def wrapper(*arg, **kw):
            signal.signal(signal.SIGALRM, __timiout_handler)
            signal.alarm(seconds)
            ret = ""
            try:
                ret = func(*arg, **kw)
            except TimeoutError,e:
                print "TimeoutError: ", e
                print "{name} ran more than {seconds}s.".format(name=func.__name__, seconds=seconds)
            except Exception,e:
                print "Error: ",e
            finally:
                signal.alarm(0)
            return ret
        return wrapper
    return decorator

