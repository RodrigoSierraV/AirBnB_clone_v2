#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
   the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a compressed archive"""

    local("sudo mkdir -p versions")
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    archive = 'versions/web_static_{}.tgz'.format(date)
    local("sudo tar -zvcf {} web_static".format(archive))

    return archive
