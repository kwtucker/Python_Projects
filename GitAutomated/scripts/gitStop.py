#!/usr/bin/env python
def gitstop():
    import subprocess, signal, os
    # This will look at all the processs that are goin to your computer
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    # Loop through the split lines and checks if it contains the gitStarted.py
    for line in out.splitlines():
        if 'gitStarted.py' in line:
            # in the 0 index is the process Id and sets that to pid
            pid = int(line.split(None, 1)[0])
            # os.kill will stop the process with the process id we set
            os.kill(pid, signal.SIGKILL)

if __name__ == '__main__':
    gitstop()