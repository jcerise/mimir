import json
import os

import shutil

import datetime


class MimirHandler():

    def __init__(self):
        pass

    def handle(self, action):
        """
        Handles a given action by building a function to call for the action
        :param action:
        :return:
        """
        action_handler = '_' + action
        handler = getattr(self, action_handler)
        handler()

    @staticmethod
    def _init():
        """
        Initialize a new mimir, creating a .mimir directory, an initial configuration file, and a notes file
        :return:
        """
        working_dir = os.getcwd()
        mimir_dir = working_dir + '/.mimir'
        config_name = '.mimir_config'
        config_location = mimir_dir + '/' + config_name
        notes_name = 'mimir_notes.txt'
        notes_location = mimir_dir + '/' + notes_name

        print 'Initializing mimir in {}...'.format(working_dir)
        try:
            if not os.path.exists(mimir_dir):
                # Attempt to make the .mimir directory in the current working directory
                os.makedirs(mimir_dir)

                # Setup the base configuration dictionary. This will be written to the config file as json. The user
                # will have control over editing these settings.
                config = {"editor":"", "tag_symbol": "@", "encrypt":False}

                # If the above directory creation succeeded, attempt to create the base configuration file
                # (.mimir/.mimir_config)
                with open(config_location, 'w+') as f:
                    json.dump(config, f)

                # Finally, create the actual notes file
                with open(notes_location, 'w+') as f:
                    current_time = datetime.date.today()
                    f.write('{:%Y-%m-%d %H:%M} Mimir initialized.'.format(current_time))

                print 'Successfully created a new mimir at {}'.format(mimir_dir)
            else:
                print 'A mimir directory already exists at {}! Aborting...'.format(mimir_dir)
                return
        except OSError as ex:
            print 'Something went wrong during initialization...'

    @staticmethod
    def _delete():
        """
        Delete any found mimirs in the given directory.
        :return:
        """
        working_dir = os.getcwd()
        mimir_dir = working_dir + '/.mimir'

        try:
            if os.path.exists(mimir_dir):
                print 'Deleting mimir at {}'.format(mimir_dir)
                shutil.rmtree(mimir_dir)
            else:
                print 'No mimir found!'
        except OSError as ex:
            print 'Something went wrong attempting to delete this mimir...'

    @staticmethod
    def _new():
        """
        Create a new note entry in the mimir_notes.txt file
        :return:
        """
        print "New called"

    @staticmethod
    def handler_not_found():
        print 'Handler not found!'


