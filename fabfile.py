from fabric.api import local, cd, run, put, env

env.hosts = ['nathan@nathanemyers.com']

def deploy():
    deploy_dir = '/home/nathan/homepage/'
    local('nathanemyers/manage.py test nathanemyers')
    run('mkdir -p ' + deploy_dir + 'nathanemyers/')
    run('mkdir -p ' + deploy_dir + 'nbapowerranks/')
    put('nathanemyers/nathanemyers/*.py', deploy_dir + 'nathanemyers/' )
    put('nathanemyers/nbapowerranks/*.py', deploy_dir + 'nbapowerranks/' )
    put('nathanemyers/manage.py', deploy_dir )

