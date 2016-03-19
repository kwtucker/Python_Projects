#!/usr/bin/env python
def git():
    import subprocess, os, time
    # Change directory out of the scripts directory and look in the GitAutomated Directory
    os.chdir('../')

    # Listing all the directories in the GitAutomated directory as a Array
    repos = os.listdir('.')

    # Invoke a array
    arr = list()

    # For each in the repos array
    for r in repos:
        # ignore any files or directories that have a dot or the scripts name
        if '.' not in r and r != 'scripts':
            # Add them to the arr array
            arr.append(r)
            # Go into that directory
            os.chdir(r)

            # List all in that directory
            subrep = os.listdir('.')

            # if it contains .git that means its a repository
            if '.git' in subrep:
                # Default message until version 2
                message = "'Git Automated Commit'"

                # Git add all the untracked and tracked changes
                subprocess.Popen(['git','add', '-A'])
                # wait 1 second
                time.sleep(1)
                # git commit with default message
                subprocess.Popen(['git', 'commit', '-m', message])
                # sleep another second
                time.sleep(1)

if __name__ == '__main__':
    git()