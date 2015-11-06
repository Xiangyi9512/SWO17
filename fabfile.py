from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run


def pre_deploy():
    local("ls -a")
    local("git add -A")
    local("git commit -m 'test fab function'")
    local("git push")

