from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run


def pre_deploy():
    local("ls -a")
    local("git add -A")
    local("git commit -m 'test fab function'")
    local("git push")


def deploy():
	pre_deploy()
	connected()


def connected():
	local("ssh xinzhang@newgate.cs.ucl.ac.uk")
	run("ssh localuser@studvm96-p.cs.ucl.ac.uk")