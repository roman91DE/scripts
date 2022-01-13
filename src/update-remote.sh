#!/bin/sh

DIR="/Users/rmn/github"
cd $DIR

LIST=$(cat remote.txt)

for REPO in $LIST
    do
        cd ${REPO}
        echo "Updating repository ${REPO}"
        git pull
        git add *; git commit -m "$(date): update-remote.sh"; git push
        cd ${DIR}
    done


