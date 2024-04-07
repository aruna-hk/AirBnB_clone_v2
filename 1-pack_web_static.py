#!/usr/bin/python3
"""
    pack web static web pages for upload
    to  the server
"""

from os import path
from datetime import datetime
from fabric.api import local


def do_pack():

    """create web pages archive to upload to server."""

    now = datetime.utcnow().strftime("%Y%M%D%H%M%S").replace('/', '')

    tarball = "web_static_{}.tgz".format(now)

    if path.isdir("versions") is False:
        local("mkdir versions")
    tar_path = "versions" + "/" + tarball
    print("Packing web_static to {}".format(tar_path))
    if local("tar -cvzf {} web_static".format(tar_path)):
        print("\nDone.")
        return tar_path

    return None
