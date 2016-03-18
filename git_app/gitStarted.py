#!/usr/bin/env python

import sys, urllib2, sched, time, os, json, git_add, git_push, gitStop



s = sched.scheduler(time.time, time.sleep)

def settings_check(sc):

    #print "Your Settings"

    x = urllib2.urlopen('http://localhost:5000/api/settings/'+ str(sys.argv[1]) + '/' + sys.argv[2])
    def curlAPI(arg1, arg2):
        # print x.read()
        resObj = dict(json.load(x))
        if resObj['gitAddCommit'] == 404:
            gitStop.gitstop()
        else:
            gAc = int(resObj['gitAddCommit'])
            gPu = int(resObj['gitPush'])
            #print "Git Add Commit: " + str(gAc) + "\n"
            #print "Git Push: " + str(gPu) + "\n"
            if gAc == 1:
                git_add.git()
            if gPu == 1:
                git_push.gitpush()

    curlAPI(sys.argv[1], sys.argv[2])

    sc.enter(10, 1, settings_check, (sc,))




if __name__ == '__main__':
    #enter(delay, priority, action, argument)
    s.enter(10, 1, settings_check, (s,))
    s.run()
