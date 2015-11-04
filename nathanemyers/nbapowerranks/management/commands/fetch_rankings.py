from django.core.management.base import BaseCommand, CommandError
from nbapowerranks.models import Team, Ranking
from bs4 import BeautifulSoup
import urllib2
import json

class Command(BaseCommand):
    help = 'Fetches the weekly ranking data from espn. If no week is specified, fetch rankings from the current week'

    def add_arguments(self, parser):
        parser.add_argument('week', nargs='?', type=int)
        parser.add_argument('--week',
                action='store',
                type=int,
                dest='week',
                nargs='?',
                help='Fetch the specified week')

    def handle(self, *args, **options):
        # temp data
        week = 1



    def add_teams():
        with open('nbapowerranks/teams.json') as data_file:
            data = json.load(data_file)

        for team in data['teams']:
            print 'Adding team: ' + team['name']
            team = Team(name=team['name'], region=team['city'], conference=team['conference'])
            team.save()



        #teamdata['dates'].append(str(week))
        #url = 'http://espn.go.com/nba/powerrankings/_/week/' + str(week)
        #print 'Getting URL: ' + url
        #response = urllib2.urlopen(url)
        #html = response.read()
        #soup = BeautifulSoup(html)

        #table = soup.find('table')
        #rows = table.find_all('tr')

        #for row in rows:
            #cols = row.find_all('td')
            #if (len(cols) > 2):
                #rank = cols[0].string
                #team_col = cols[1].find('div', style="padding:10px 0;")
                #if (team_col):
                    #city = team_col.find('a').string
                    #team_img = cols[1].find('a').get('href')
                    #addRank(city, team_img, rank, week - 1)

    #def addRank(team_name, team_img, rank, date_index):
        #for team in teamdata['teams']:
            #if team['city'] == team_name:
                #if (team_name == 'Los Angeles' and team['name'] == 'Lakers' and ( 'lakers' in team_img )):
                    #team['values'].append({ 'date': date_index, 'ranking': rank })
                    #break;
                #elif (team_name == 'Los Angeles' and team['name'] == 'Clippers' and ( 'clippers' in team_img )):
                    #team['values'].append({ 'date': date_index, 'ranking': rank })
                    #break;
                #elif (team_name != 'Los Angeles'):
                    #team['values'].append({ 'date': date_index, 'ranking': rank })
                    #break;
