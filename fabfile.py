from fabric.contrib.files import append, exists, sed
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm


def pre_deploy():
    local("ls -a")
    local("git add -A")
    local("git commit -m 'test fab function'")
    local("git push")


def deploy():
	pre_deploy()
	connected()


def connected():
	code_dir = '/var/www/html'
    	with cd(code_dir):
        	run("git clone ")
        	run("touch app.wsgi")