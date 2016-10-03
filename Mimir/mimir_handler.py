import json
import os

import shutil


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

    def _init(self):
        """
        Initialize a new mimir, creating a .mimir directory and an initial configuration file
        :return:
        """
        working_dir = os.getcwd()
        mimir_dir = working_dir + '/.mimir'
        config_name = '.mimir_config'
        config_location = mimir_dir + '/' + config_name

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
                print 'Successfully created a new mimir at {}'.format(mimir_dir)
            else:
                print 'A mimir directory already exists at {}! Aborting...'.format(mimir_dir)
                return
        except OSError as ex:
            print 'Something went wrong during initialization...'

    def _delete(self):
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
    def handler_not_found():
        print 'Handler not found!'


