#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

    from django.core.management import execute_from_command_line

    # execute_from_command_line(sys.argv)


# secondary code that didn't work
# manage.py

# from flask.ext.script import Manager
#
# from app import app
#
# manager = Manager(app)
#
# @manager.command
# def migrate(action):
#     from flask.ext.evolution import Evolution
#     evolution = Evolution(app)
#     evolution.manager(action)
#
# if __name__ == "__main__":
#     manager.run()
