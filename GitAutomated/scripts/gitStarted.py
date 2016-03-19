#!/usr/bin/env python
import sys, urllib2, sched, time, os, json, git_add, git_push, gitStop, datetime

# This will set the current time
dt = datetime.datetime.now()

# Schedule time and how long sleep
s = sched.scheduler(time.time, time.sleep)

# Grab the settins from server
def settings_check(sc):
    # Server API call with dynamic params.
    x = urllib2.urlopen('http://localhost:5000/api/settings/'+ str(sys.argv[1]) + '/' + sys.argv[2])

    # parse the settings and start pythons settings scripts
    def curlAPI():
        # Putting the response to a json object or dict
        resObj = dict(json.load(x))
        # if response constains a value of 404 stop the background process
        if resObj['gitAddCommit'] == 404:
            # calls the stop process
            gitStop.gitstop()
        else:
            # set the values of these keys to a variable
            gAc = int(resObj['gitAddCommit'])
            gPu = int(resObj['gitPush'])

            # If the value is set to on, call the script
            if gAc == 1:
                git_add.git()
            if gPu == 1:
                # Call this command at 12pm-1pm or 5pm-6pm
                if dt.hour >= 12 and dt.hour <= 13:
                    git_push.gitpush()
                if dt.hour >= 17 and dt.hour <= 18:
                    git_push.gitpush()


    curlAPI()
    # Every 30 min(1800) the settings will be checked
    # Every 15 min(900) the settings will be checked
    sc.enter(900, 1, settings_check, (sc,))


if __name__ == '__main__':
    #enter(delay, priority, action, argument)
    s.enter(900, 1, settings_check, (s,))
    s.run()
