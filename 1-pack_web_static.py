#!/usr/bin/python3
""" prepares files for deployment """
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """creating archive to deploy"""

    date = datetime.utcnow()
    now = str(date.year) + str(date.mont) + str(date.day) + str(date.hour) + \
            str(date.minute) + str(date.second)
    file = "versions/web_static_{}.tgz".format(now)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
