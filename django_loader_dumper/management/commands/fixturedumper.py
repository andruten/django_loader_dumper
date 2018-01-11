import re
from django.core.management.base import BaseCommand
from django.core.serializers import serialize
from django.apps import apps
import os


class Command(BaseCommand):

    help = "Fixture Dumper. Export models to fixtures."
    format = 'json'

    def __init__(self, stdout=None, stderr=None, no_color=False):
        super(Command, self).__init__(stdout, stderr, no_color)
        self.indent = None

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('app_name',
                            nargs='*',
                            help='Provide app names as is listed in INSTALLED_APPS. '
                                 'If no app_name provided, will dump everything',
                            type=str)

        parser.add_argument('--indent',
                            dest='indent',
                            type=int,
                            help='JSON indentation files.', )

    def get_json_filename(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
        return "{0}.json".format(re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower())

    def get_app_names(self):
        return list(set([model._meta.app_label for model in apps.get_models()]))

    def dump(self, model, app_name, to_file):
        self.stdout.write("\t{0}:".format(model.__name__))
        self.stdout.write("\t- Serializing {0} objects...".format(model.objects.all().count()), ending="")
        self.stdout.flush()
        serialized_data = serialize(self.format, model.objects.all(), indent=self.indent)
        self.stdout.write(" [ OK ]")
        self.stdout.write("\t- Dumping in {0}/fixtures/{1}...".format(app_name, to_file), ending="")
        self.stdout.flush()
        with open("{0}/fixtures/{1}".format(app_name, to_file), 'w+') as fixture_file:
            fixture_file.write(serialized_data)
            self.stdout.write(" [ OK ]")

    def handle(self, *args, **options):
        self.indent = options["indent"]
        dump_app_names = options["app_name"] if options["app_name"] else self.get_app_names()
        for app_name in dump_app_names:
            self.stdout.write("{0}".format(app_name))
            app_models = apps.get_app_config(app_name).get_models()
            for model in app_models:
                os.makedirs(os.path.dirname("{0}/fixtures/".format(app_name)), exist_ok=True)
                self.dump(model, app_name, self.get_json_filename(model.__name__))
