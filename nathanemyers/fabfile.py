from fabric.api import local, cd, run, put, env

env.hosts = ['nathan@nathanemyers.com']

def deploy():
    deploy_dir = '/home/nathan/homepage/'
    local('./manage.py test')
    local('sass --update nathanemyers/sass:nathanemyers/static/css/')
    local('find . -name "*.pyc" -exec rm -rf {} \;')
    run('mkdir -p ' + deploy_dir + 'nathanemyers/')
    run('mkdir -p ' + deploy_dir + 'nbapowerranks/')
    put('nathanemyers/*.py', deploy_dir + 'nathanemyers/' )
    put('nathanemyers/static', deploy_dir + 'nathanemyers/' )
    put('nathanemyers/templates', deploy_dir + 'nathanemyers/' )

    put('nbapowerranks/*.py', deploy_dir + 'nbapowerranks/' )
    put('nbapowerranks/cron', deploy_dir + 'nbapowerranks/' )
    put('nbapowerranks/static', deploy_dir + 'nbapowerranks/' )
    put('nbapowerranks/templates', deploy_dir + 'nbapowerranks/' )
    put('nbapowerranks/management', deploy_dir + 'nbapowerranks/' )
    put('nbapowerranks/data', deploy_dir + 'nbapowerranks/' )
    put('nbapowerranks/migrations', deploy_dir + 'nbapowerranks/' )

    put('manage.py', deploy_dir )
    run('sudo python ' + deploy_dir + 'manage.py collectstatic')
    run('sudo service apache2 restart')

