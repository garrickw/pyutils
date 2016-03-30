from timeCtrl import timeit, timeout
import time


@timeit
def test1():
    print "test1"
    time.sleep(3)

@timeout(4)
def test2():
    print "test2"
    time.sleep(3)
    print "not timeout"

@timeout(3)
def test3():
    print "test3"
    time.sleep(4)
    print "oops!!"  #it should nerver been here


if __name__ == "__main__":
    print "timeit test"
    test1()
    print 
    print "timeout test"
    test2()
    print 
    test3()


#output:
#timeit test
#test1
#test1 costs 3.00309705734s.
#
#timeout test
#test2
#not timeout
#
#test3
#TimeoutError:  Time out.
#test3 ran more than 3s.
