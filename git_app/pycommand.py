#!/usr/bin/env python

import sys,urllib2, sched, time, os, git_add, json

s = sched.scheduler(time.time, time.sleep)

def settings_check(sc):

    print "Your Settings"

    x = urllib2.urlopen('http://localhost:5000/api/settings')
    def curlAPI(arg):
        # print x.read()

        git_add.git(x.read())
    curlAPI(sys.argv[1])

    sc.enter(10, 1, settings_check, (sc,))




if __name__ == '__main__':
    s.enter(10, 1, settings_check, (s,))
    s.run()
