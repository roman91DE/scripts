#!/bin/bash

# destination
THUMBDRIVE_PATH="/media/rmn/46DD-C172/BACKUP.tar.gz"

# origin
DRIVE_PATH="/run/user/1000/gvfs/ftp:host=fritz.box/RMN"

# directories
DIRS=(accounting docs financial security)


for DIR in ${DIRS[@]}; do
   tar -czvf ${THUMBDRIVE_PATH} $DRIVE_PATH/$DIR
done;


# compresses DRIVE_PATH to THUMBDRIVE_PATH
#
