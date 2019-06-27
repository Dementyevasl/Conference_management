import json

from django.core.management.base import BaseCommand
from conference.models import Conference
from tqdm import tqdm


class Command(BaseCommand):

    def read_json(self, path):
        with open(path) as json_file:
            data = json.load(json_file)
        return data

    def import_conference(self, data):
        kwargs = {}
        for key, val in data[1].items():
            if key in ['conferenceID', 'acceptance rate']:
                continue
            key = '_'.join(key.split(' '))
            if type(val) is dict:
                for val_key in val.keys():
                    new_key = '{}_{}'.format(key, val_key)
                    kwargs[new_key] = val[val_key]
            elif type(val) is list:
                new_val = ','.join(str(x) for x in val)
                kwargs[key] = new_val
            else:
                kwargs[key] = val
        del_keys = [key for key, val in kwargs.items() if val == '']
        for key in del_keys:
            kwargs.pop(key, None)
        c = Conference(**kwargs)
        c.save()

    def handle(self, *args, **options):
        paths = [
            # 'data_file.json',
            # 'data_file2.json',
            'all_conferences.json'
        ]
        for path in paths:
            data = self.read_json(path)
            for conference in data.items():
                self.import_conference(conference)