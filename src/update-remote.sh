#!/bin/sh

DIR="~/github"
cd ${DIR}



for REPO in remote.txt
    do
        cd ${REPO}
        echo "Updating repository ${REPO}"
        git pull
        git add * & git commit -m "$(date): update-remote.sh" & git push
        cd ${DIR}
    done


