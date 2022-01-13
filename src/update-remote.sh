#!/bin/sh

DIR="/Users/rmn/github"
REMOTE_FILE="${DIR}/remote.txt"

cd $DIR

if [ ! -f "$REMOTE_FILE" ]; then
    echo "Create remote.txt as a list of remote repositories"
    exit
fi


LIST=$(cat remote.txt)

for REPO in $LIST
    do
        cd ${REPO}
        echo "Updating repository ${REPO}"
        git pull
        git add *; git commit -m "$(date): update-remote.sh"; git push
        cd ${DIR}
    done


