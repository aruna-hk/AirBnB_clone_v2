#!/usr/bin/python3
"""
   server deployment with fabric
   FULL DEPLOYMENT
   create archive and distribute to the servers
"""
from fabric.api import local, env, run, put, runs_once
from os import path
from datetime import datetime
env.hosts = ['web-01', 'web-02']
env.user = "ubuntu"
env.key_filename = "/home/x230/.ssh/school"


@runs_once
def do_pack():
    """
        pack web pages to .tgz file for upload
    """
    now = datetime.utcnow().strftime("%Y%m%d%H%M%S").replace('/', '')

    if path.isdir("versions") is False:
        local("rm -f versions")
        mkdir("versions")
    version = "versions/web_static_" + now + ".tgz"
    if (local("tar -cvzf {} web_static".format(version)).succeeded):
        return version
    return None


def do_deploy(archive_path):
    """
        deploy the archive, untar and point the server symlink
        to latest deployed version
    """

    if path.exists(archive_path):
        remote = "/tmp/{}".format(archive_path.split('/')[1])
        put(remote_path="/tmp/", local_path=archive_path)
        release_dir = "/data/web_static/releases/" + \
            archive_path.split('.')[0].split('/')[1] + "/"
        run("mkdir -p {}".format(release_dir))
        run("tar -xzf {} -C {}".format(remote, release_dir))
        run("rm -f {}".format(remote))
        run("rm -rf /data/web_static/current")
        run("mv {}web_static/* {}".format(release_dir, release_dir))
        run("rm -rf {}web_static".format(release_dir))
        run("ln -s {} /data/web_static/current".format(release_dir))
        print("New version deployed!")
        return True
    return False


@runs_once
def deploy():
    """ full deployment"""

    tarball = do_pack()
    if (tarball is None):
        return False

    for host in env.hosts:
        env.host_string = host
        deployed = do_deploy(tarball)

    return deployed