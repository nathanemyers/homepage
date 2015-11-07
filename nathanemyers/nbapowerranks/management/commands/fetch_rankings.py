from django.core.management.base import BaseCommand, CommandError
from nbapowerranks.models import Team, Ranking
from bs4 import BeautifulSoup, NavigableString
import urllib2
import json
import re

import pdb

def stripTags(html, invalid_tags):
    for tag in html:
        if tag.name in invalid_tags:
            s = ""
            for c in tag.contents:
                if not isinstance(c, NavigableString):
                    c = stripTags(unicode(c), invalid_tags)
                s += unicode(c)

            tag.replaceWith(s)
    return html

def resolve_team(team_html_link):
    if ('los-angeles-lakers' in team_html_link):
        return Team.objects.get(name='Lakers')
    if ('los-angeles-clippers' in team_html_link):
        return Team.objects.get(name='Clippers')
    if ('warriors' in team_html_link):
        return Team.objects.get(name='Warriors')
    if ('cavaliers' in team_html_link):
        return Team.objects.get(name='Cavaliers')
    if ('spurs' in team_html_link):
        return Team.objects.get(name='Spurs')
    if ('thunder' in team_html_link):
        return Team.objects.get(name='Thunder')
    if ('rockets' in team_html_link):
        return Team.objects.get(name='Rockets')
    if ('grizzlies' in team_html_link):
        return Team.objects.get(name='Grizzlies')
    if ('hawks' in team_html_link):
        return Team.objects.get(name='Hawks')
    if ('heat' in team_html_link):
        return Team.objects.get(name='Heat')
    if ('bulls' in team_html_link):
        return Team.objects.get(name='Bulls')
    if ('pelicans' in team_html_link):
        return Team.objects.get(name='Pelicans')
    if ('raptors' in team_html_link):
        return Team.objects.get(name='Raptors')
    if ('celtics' in team_html_link):
        return Team.objects.get(name='Celtics')
    if ('bucks' in team_html_link):
        return Team.objects.get(name='Bucks')
    if ('wizards' in team_html_link):
        return Team.objects.get(name='Wizards')
    if ('pacers' in team_html_link):
        return Team.objects.get(name='Pacers')
    if ('pistons' in team_html_link):
        return Team.objects.get(name='Pistons')
    if ('jazz' in team_html_link):
        return Team.objects.get(name='Jazz')
    if ('kings' in team_html_link):
        return Team.objects.get(name='Kings')
    if ('suns' in team_html_link):
        return Team.objects.get(name='Suns')
    if ('mavericks' in team_html_link):
        return Team.objects.get(name='Mavericks')
    if ('hornets' in team_html_link):
        return Team.objects.get(name='Hornets')
    if ('magic' in team_html_link):
        return Team.objects.get(name='Magic')
    if ('knicks' in team_html_link):
        return Team.objects.get(name='Knicks')
    if ('wolves' in team_html_link):
        return Team.objects.get(name='Timberwolves')
    if ('nuggets' in team_html_link):
        return Team.objects.get(name='Nuggets')
    if ('blazers' in team_html_link):
        return Team.objects.get(name='Trail Blazers')
    if ('nets' in team_html_link):
        return Team.objects.get(name='Nets')
    if ('76ers' in team_html_link):
        return Team.objects.get(name='76ers')

class Command(BaseCommand):
    help = 'Fetches the weekly ranking data from ESPN. If no week is specified, fetch rankings from the current week'

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
        week = 0

        url = 'http://espn.go.com/nba/powerrankings/_/week/' + str(week)
        print 'Getting URL: ' + url
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table')

        # Figure out what week we're looking at
        table_head = table.find('tr', 'stathead').find('td').getText()
        m = re.search('Rankings: (Preseason|Week \w+)', table_head)
        matched_week = m.group(1)
        if (matched_week == 'Preseason'):
            week = 0
        else:
            week = int(re.search('Week (\w+)', matched_week).group(1))

        rows = table.find_all('tr', ['evenrow', 'oddrow'])

        for row in rows:
            cols = row.find_all('td')
            rank = cols[0].string

            city_col = cols[1].find_all('a')
            # this is the link to the team's detail page, 
            # we can use this to differentiate between the Clippers and the Lakers
            team_html_link = city_col[0].get('href') 

            team = resolve_team(team_html_link)

            comment = stripTags(cols[3], ['b', 'i', 'a', 'u'])
            comment_string = comment.getText()

            rank_object = Ranking(
                    year = '2016',
                    rank = rank,
                    team = team,
                    summary = comment_string,
                    week = week
                    )
            rank_object.save()


    def addRank(team_name, team_img, rank, date_index):
        for team in teamdata['teams']:
            if team['city'] == team_name:
                if (team_name == 'Los Angeles' and team['name'] == 'Lakers' and ( 'lakers' in team_img )):
                    team['values'].append({ 'date': date_index, 'ranking': rank })
                    break;
                elif (team_name == 'Los Angeles' and team['name'] == 'Clippers' and ( 'clippers' in team_img )):
                    team['values'].append({ 'date': date_index, 'ranking': rank })
                    break;
                elif (team_name != 'Los Angeles'):
                    team['values'].append({ 'date': date_index, 'ranking': rank })
                    break;

    def add_teams():
        with open('nbapowerranks/teams.json') as data_file:
            data = json.load(data_file)

        for team in data['teams']:
            print 'Adding team: ' + team['name']
            team = Team(name=team['name'], region=team['city'], conference=team['conference'])
            team.save()
