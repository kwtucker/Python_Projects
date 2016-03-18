#!/usr/bin/env python

import sys,urllib2, sched, time, os, git_add, git_push, json



s = sched.scheduler(time.time, time.sleep)

def settings_check(sc):

    print "Your Settings"

    x = urllib2.urlopen('http://localhost:5000/api/settings/'+ str(sys.argv[1]) + '/' + sys.argv[2])
    def curlAPI(arg1, arg2):
        # print x.read()
        resObj = dict(json.load(x))
        # if resObj['Error']:

        #     # os.getpid()
        #     # for process in psutil.process_iter():
        #     #     if process.cmdline == ['python', 'gitStarted.py', sys.argv[1], sys.argv[2]]:
        #     #         print('Process found. Terminating it.')
        #     #         process.terminate()
        #     #         break
        #     # else:
        #     #     print('Process not found: starting it.')
        #     #     Popen(['python', 'StripCore.py'])
        #     print "Bad Command"

        # if resObj['gitAddCommit']:
        gAc = int(resObj['gitAddCommit'])
        gPu = int(resObj['gitPush'])
        print "Git Add Commit: " + str(gAc) + "\n"
        print "Git Push: " + str(gPu) + "\n"
        if gAc == 1:
            git_add.git()
        if gPu == 1:
            git_push.gitpush()


        # git_add.git(x.read())
    curlAPI(sys.argv[1], sys.argv[2])

    sc.enter(10, 1, settings_check, (sc,))




if __name__ == '__main__':
    s.enter(10, 1, settings_check, (s,))
    s.run()
