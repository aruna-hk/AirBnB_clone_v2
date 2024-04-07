#!/usr/bin/python3
"""
    pack web static web pages for upload
    to  the server
"""

from os import path, mkdir
from datetime import datetime
from fabric import task
from invoke import run


@task
def do_pack(c):

    """Create a tar gzipped archive of the directory web_static."""
    now = datetime.utcnow().strftime("%Y%M%D%H%M%S").replace('/', '')
    tarball = "web_static_{}.tgz".format(now)
    if path.isdir("versions") is False:
        run("mkdir -p versions")
    tar_path = "versions" + "/" + tarball
    print("Packing web_static to {}\n".format(tar_path))
    if run("tar -cvzf {} web_static".format(tar_path)).exited == 0:
        print("\nDone.")
        return tar_path

    return None
