from __future__ import with_statement
from fabric.contrib.files import append, exists, sed
from fabric.api import *
from fabric.contrib.console import confirm

#test for studvm 
env.hosts = ['localuser@studvm50-p.cs.ucl.ac.uk']


def pre_deploy():
    local("ls -a")
    local("git add -A")
    local("git commit -m 'test fab function'")
    local("git push")

def github():
    local("justfortest")


#using first_deploy when this is the first timw to deploy to a new host or new directroy 
def first_deploy():
	pre_deploy()
	connected1()
#using following_deploy for the deploy after the first one
def following_deploy():
    pre_deploy()
    connected2()

def connected1():
	code_dir = '/home/localuser/Desktop'

    	with cd(code_dir):
            run("git clone https://github.com/Xiangyi9512/SWO17.git")
        run("touch app.wsgi")

def connected2():
    code_dir = '/home/localuser/Desktop/SWO17'

    with cd(code_dir):
            with settings(warn_only=True):
                if run("test -d %s" % code_dir).failed:
                    run("git clone https://github.com/Xiangyi9512/SWO17.git")
    with cd(code_dir):
            run("git pull https://github.com/Xiangyi9512/SWO17.git")
            run("touch app.wsgi")