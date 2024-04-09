#!/usr/bin/python3
"""
   preparing/ packing wb pages for upload
"""
from os import path, mkdir
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        pack web pages to .tgz file for upload
    """
    now = datetime.utcnow().strftime("%Y%M%D%H%M%S").replace('/', '')

    if path.isdir("versions") is False:
        mkdir("versions")
    version = "versions/web_static_" + now + ".tgz"
    if (local("tar -cvzf {} web_static".format(version)).succeeded):
        return version
    return None
