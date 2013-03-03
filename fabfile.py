from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['sse_temp@assu-web.stanford.edu']

def prepare_deploy():
    test()
    commit()
    push()
    
def test():
    local("python manage.py test info")

def commit():
    local("git add -p && git commit")

def push():
    local("git push")
    
def deploy():
    code_dir = '/home/sse/temp/website'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone https://github.com/tjsavage/ssetemp.git %s" % code_dir)
            
    with cd(code_dir):
        with prefix('source venv/bin/activate'):
            run("git pull origin master")
            
            
        
    
    
