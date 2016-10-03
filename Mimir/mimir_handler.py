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
        Initialize a new mimir, creating a .mimir directory and all appropriate files
        :return:
        """
        working_dir = os.getcwd()
        mimir_dir = working_dir + '/.mimir'

        print 'Initializing mimir in {}...'.format(working_dir)
        try:
            if not os.path.exists(mimir_dir):
                os.makedirs(mimir_dir)
            else:
                print 'A mimir directory already exists at {}! Aborting...'.format(mimir_dir)
        except OSError as ex:
            print 'Something went wrong during initialization...'

    def _delete(self):
        """
        Delete any found mimirs in the given directory.
        :return:
        """
        working_dir = os.getcwd()
        mimir_dir = working_dir + '/.mimir'

        print 'You are about to delete the mimir in {}'.format(working_dir)
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


