import json
import os

import shutil

import datetime


class MimirHandler:

    def __init__(self):
        self.working_dir = os.getcwd()
        self.mimir_dir = self.working_dir + '/.mimir'
        self.config_name = '.mimir_config'
        self.config_location = self.mimir_dir + '/' + self.config_name
        self.notes_name = 'mimir_notes.txt'
        self.notes_location = self.mimir_dir + '/' + self.notes_name

    def handle(self, action, **kwargs):
        """
        Handles a given action by building a function to call for the action
        :param action:
        :return:
        """
        action_handler = '_' + action
        handler = getattr(self, action_handler)
        handler(**kwargs)

    def _init(self, **kwargs):
        """
        Initialize a new mimir, creating a .mimir directory, an initial configuration file, and a notes file
        :return:
        """

        print 'Initializing mimir in {}...'.format(self.working_dir)
        try:
            if not os.path.exists(self.mimir_dir):
                # Attempt to make the .mimir directory in the current working directory
                os.makedirs(self.mimir_dir)

                # Setup the base configuration dictionary. This will be written to the config file as json. The user
                # will have control over editing these settings.
                config = {"editor":"", "tag_symbol": "@", "encrypt":False}

                # If the above directory creation succeeded, attempt to create the base configuration file
                # (.mimir/.mimir_config)
                with open(self.config_location, 'w+') as f:
                    json.dump(config, f)

                # Finally, create the actual notes file
                with open(self.notes_location, 'w+') as f:
                    current_time = datetime.datetime.now()
                    f.write('{:%Y-%m-%d %H:%M} Mimir initialized.'.format(current_time))

                print 'Successfully created a new mimir at {}'.format(self.mimir_dir)
            else:
                print 'A mimir directory already exists at {}! Aborting...'.format(self.mimir_dir)
                return
        except OSError as ex:
            print 'Something went wrong during initialization...'

    def _delete(self, **kwargs):
        """
        Delete any found mimirs in the given directory.
        :return:
        """

        try:
            if os.path.exists(self.mimir_dir):
                print 'Deleting mimir at {}'.format(self.mimir_dir)
                shutil.rmtree(self.mimir_dir)
            else:
                print 'No mimir found!'
        except OSError as ex:
            print 'Something went wrong attempting to delete this mimir...'

    def _new(self, **kwargs):
        """
        Create a new note entry in the mimir_notes.txt file
        :return:
        """
        # Check to ensure that all the requisite files/dirs exists before continuing
        if os.path.exists(self.mimir_dir) and os.path.exists(self.notes_location) and os.path.exists(self.config_location):
            note = kwargs['note']

            # If the note is a single word, it will be passed from Click as a string, if it was several words, it comes
            # across as a tuple, and we need to combine the elements to be coherent
            if isinstance(note, tuple):
                note = ' '.join(map(str, kwargs['note']))

            with open(self.notes_location, 'a') as f:
                f.write('\n\n')
                current_time = datetime.datetime.now()
                f.write('{:%Y-%m-%d %H:%M} :: {}'.format(current_time, note))

            print '[Entry added to mimir at {}]'.format(self.mimir_dir)
        else:
            print 'No mimir found, or files missing...are you sure you are in the correct dir? ({})'\
                .format(self.working_dir)

    @staticmethod
    def handler_not_found():
        print 'Handler not found!'


