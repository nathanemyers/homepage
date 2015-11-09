from fabric.api import local, cd, run, put, env

env.hosts = ['nathan@nathanemyers.com']

def deploy():
    deploy_dir = '/home/nathan/homepage/'
    local('./manage.py test')
    local('sass --update nathanemyers/sass:nathanemyers/static/css/')
    run('mkdir -p ' + deploy_dir + 'nathanemyers/')
    run('mkdir -p ' + deploy_dir + 'nbapowerranks/')
    put('nathanemyers/*.py', deploy_dir + 'nathanemyers/' )
    put('nathanemyers/static', deploy_dir + 'nathanemyers/' )
    put('nathanemyers/templates', deploy_dir + 'nathanemyers/' )
    put('nbapowerranks/*.py', deploy_dir + 'nbapowerranks/' )
    put('nbapowerranks/cron', deploy_dir + 'nbapowerranks/' )
    put('manage.py', deploy_dir )
    run('sudo python ' + deploy_dir + 'manage.py collectstatic')

