# Django Loader Dumper

Commands for loading and dumping fixtures based on installed app names inspection.

## Requirements

* Python (3.4, 3.5, 3.6)
* Django (1.8, 1.9, 1.10, 1.11, 2.0)

## Installation

Install using `pip`...

    pip install django-loader-dumper

Add `'django_loader_dumper'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'django_loader_dumper',
    )

## Example

Startup up a new project like so...

    pip install django
    pip install django_loader_dumper

After creating some data in your database, then you have to call commands like this:
    
    $ ./manage.py fixturedumper app_name_1 app_name_2 ...
    $ ./manage.py fixtureloader app_name_1 app_name_2 app_name_3

If no app_name provided, all app's models will be dumped/loaded. All fixtures will be created inside your project in `fixtures/app_name` by default.

Parameter `--indent` can also be provided to the commands.
Parameter `--exportpath` can also be provided to the commands if you don't like the default fixtures/ path.

NOTE: Django application `contenttypes` is excluded from this commands because when Django migrates your projects doesn't applies them in the same order. 

Enjoy :).
