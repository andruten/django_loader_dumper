# Django Loader Dumper

Commands for loading and dumping fixtures based on app names.

## Requirements

* Python (3.4, 3.5, 3.6)
* Django (1.8, 1.9, 1.10, 1.11, 2.0)

## Installation

Install using `pip`...

    pip install django_loader_dumper

Add `'django_loader_dumper'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'django_loader_dumper',
    )

## Example

Startup up a new project like so...

    pip install django
    pip install django_loader_dumper

Now you have to call commands like this:
    
    $ ./manage.py fixturedumper app_name_1 app_name_2 app_name_3
    $ ./manage.py fixtureloader app_name_1 app_name_2 app_name_3

Enjoy :).
