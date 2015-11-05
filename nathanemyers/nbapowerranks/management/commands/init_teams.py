#!/usr/bin/python
import json
from nbapowerranks.models import Team
from django.core.management.base import BaseCommand, CommandError

# example data format:
  #'teams': [
        #{
          #'city': 'Golden State',
          #'name': 'Warriors',
          #'values': [],
          #'color': '#FDB927',
          #'conference': 'Western',
          #'division': 'Pacific'
        #}, ...
    #]


class Command(BaseCommand):
    #def add_arguments(self, parser):

    def handle(self, *args, **options):
        with open('nbapowerranks/teams.json') as data_file:
            data = json.load(data_file)

        print 'Loading Teams...'
        for team in data['teams']:
            print team['name']
            team = Team(name=team['name'], region=team['city'], conference=team['conference'])
            team.save()

        print 'Done!'
