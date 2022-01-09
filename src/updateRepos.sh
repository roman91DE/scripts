#!/bin/sh


cd ~/github

REPOS=$(/bin/ls)
# COUNTER=0

for REPO in $REPOS
    do
        cd $REPO
        git pull & git add * & git commit -m "updateRepo.sh" & git push
        # COUNTER=$($COUNTER+1)
        cd ..
    done

# echo "Done - updated ${COUNTER} repositories!"
