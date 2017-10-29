#!/usr/bin/python

class Hello(object):

    def hellothere(self, tp):
	print "Hello there: {}".format(tp)


if '__name__' == '__main__':
    h = Hello()
    h.hellothere("Is it")
