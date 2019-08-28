#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
   the contents of the web_static folder
"""

from fabric.api import local, run, env, put
from datetime import datetime
from os.path import exists
env.hosts = ['104.196.135.55', '34.73.16.217']
env.user = 'ubuntu'


def do_pack():
    """Generates a compressed archive"""

    local("sudo mkdir -p versions")
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    archive = 'versions/web_static_{}.tgz'.format(date)
    local("sudo tar -zvcf {} web_static".format(archive))

    return archive


def do_deploy(archive_path):
    """Deploy an archive in a webserver"""

    if exists(archive_path) is False:
        return False

    try:

        put(archive_path, '/tmp/')
        arch = archive_path.split('/')[-1]
        ubi = arch.split('.')[0]
        path = '/data/web_static/releases/'
        run('mkdir -p {}{}/'.format(path, ubi))
        run('tar -zxf /tmp/{} -C {}{}/'.format(arch, path, ubi))
        run('rm /tmp/{}'.format(arch))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, ubi))
        run('rm -rf {}{}/web_static'.format(path, ubi))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, ubi))

        return True
    except:
        return False


def deploy():
    """reates and distributes an archive to your web servers"""

    if do_pack():
        return do_deploy(do_pack())
    return False
