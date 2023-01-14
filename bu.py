#! /usr/bin/python3
# a python script that backups folder and files from root directory

import os
import sys
from datetime import date
import logging


args = sys.argv
logging.basicConfig(format='%(levelname) s%(message)s', filename='backup.log', filemode='a', level=logging.INFO,)
clr = ['\033[1;32m', '\033[m']

if len(args) > 2:
    raise Exception('pass avalid relative path')

else:
    try:
        today = date.today()

        # folder on the home dir to be backedup
        folder = sys.argv[1]

        # command that backs up the sepcified folder
        os.system(f'tar -czvf {today}-Backup.tar.gz /{folder}')

        # current working dir
        Cwd = os.getcwd()

        # destination working dir
        backup_files_dir = os.path.join(Cwd, 'backup_files')
        if not os.path.exists(backup_files_dir):
            os.mkdir(backup_files_dir)

        # move backup file from Cwd to destination dir
        os.system(f'mv {today}-Backup.tar.gz {backup_files_dir}')

        # apt update
        os.system("sudo apt-get update >> backup.log")

        print (f"{clr[0]}{folder}_dir Backup and system update sucessfully compelected{clr[1]}")
        logging.info(f" |{folder}_dir Backup and system update sucessfully compelected \n")

    except:
        print ('there was a problem somewhere')
