#!/usr/bin/python3
"""
   server deployment with fabric
   FULL DEPLOYMENT
   create archive and distribute to the servers
"""
from fabric.api import local, env, run, put
from os import path
from datetime import datetime
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['web-01']


def deploy():
    """ full deployment"""

    tarball = do_pack()
    if (tarball is None):
        return False
    env.hosts = ['web-01', 'web-02']
    env.user = "ubuntu"
    env.key_filename = "/home/x230/.ssh/school"

    for host in env.hosts:
        env.host_string = host
        deployed = do_deploy(tarball)
    return deployed
