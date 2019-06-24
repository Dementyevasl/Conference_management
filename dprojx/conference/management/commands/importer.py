import json

from django.core.management.base import BaseCommand
from conference.models import Conference


class Command(BaseCommand):

    def read_json(self, path):
        with open(path) as json_file:
            data = json.load(json_file)
        return data

    def import_conference(self, data):
        kwargs = {}
        for key, val in data.items():
            key = '_'.join(key.split(' '))
            if type(val) is dict:
                for val_key in val.keys():
                    new_key = '{}_{}'.format(key, val_key)
                    kwargs[new_key] = val[val_key]
            elif type(val) is list:
                new_val = ','.join(val)
                kwargs[key] = new_val
            else:
                kwargs[key] = val
            del_keys = [key for key, val in kwargs.items() if val == '']
            for key in del_keys:
                kwargs.pop(key, None)
        # print(kwargs)
        # confTitle = kwargs['confTitle']
        c = Conference(**kwargs)
        # c = Conference(confTitle=confTitle)
        c.save()

    def handle(self, *args, **options):
        paths = ['data_file.json',
                 'data_file2.json']
        for path in paths:
            data = self.read_json(path)
            for conference in data:
                self.import_conference(conference)