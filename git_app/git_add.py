#!/usr/bin/env python
def git():
    import subprocess
    subprocess.Popen(['cd','../'])
    ls  = subprocess.Popen(['ls','-l'], stdout=subprocess.PIPE)
    awk = subprocess.Popen(["awk '{{print $9}}'"], stdin=ls.stdout,shell=True)
    ls.wait()
    stdout = awk.communicate()[0]
    # print stdout
    print "Git Add Commit"


# proc = subprocess.Popen(["virsh dumpxml {0} | grep 'source file' | awk -F\\' '{{print $2}}'".format(vm)], stdout=subprocess.PIPE, shell=True)
# stdout = proc.communicate()[0]

    # git a -a

if __name__ == '__main__':
    git()