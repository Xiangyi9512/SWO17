from fabric.contrib.files import append, exists, sed
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm

#the one worked with the xinzhang VM


def pre_deploy():
    local("ls -a")
    local("git add -A")
    local("git commit -m 'test fab function'")
    local("git push")


def deploy():
	pre_deploy()
	connected()


def connected():
	code_dir = '~/Desktop/test1/var'
    	with cd(code_dir):
            with settings(warn_only=True):
                if run("test -d %s" % code_dir).failed:
                    run("git clone https://github.com/Xiangyi9512/SWO17.git")
        with cd(code_dir):
            run("git pull")
            run("touch app.wsgi")