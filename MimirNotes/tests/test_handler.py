import os

import shutil
from mock import patch

from MimirNotes.mimir import Actions
from MimirNotes.mimir_handler import MimirHandler


class TestHandler:

    def test_handle_init_action(self):
        actions = Actions
        with patch.object(MimirHandler, '_init') as mock:
            handler = MimirHandler()
            handler.handle(actions.init.name)

        mock.assert_called_with()

    def test_handle_delete_action(self):
        actions = Actions
        with patch.object(MimirHandler, '_delete') as mock:
            handler = MimirHandler()
            handler.handle(actions.delete.name)

        mock.assert_called_with()

    def test_handle_new_action(self):
        actions = Actions
        with patch.object(MimirHandler, '_new') as mock:
            handler = MimirHandler()
            handler.handle(actions.new.name)

        mock.assert_called_with()

    def test_init_directory(self):
        working_dir = os.getcwd()
        mimir_dir = working_dir + '/.mimir'

        # First, remove any existing mimir dirs
        if os.path.exists(mimir_dir):
            shutil.rmtree(mimir_dir)

        handler = MimirHandler()
        handler._init()

        # Ensure the mimir dir was created
        assert os.path.exists(mimir_dir) is True

    def test_delete_mimir(self):

        working_dir = os.getcwd()
        mimir_dir = working_dir + '/.mimir'

        # First, remove any existing mimir dirs
        if os.path.exists(mimir_dir):
            shutil.rmtree(mimir_dir)

        # Create a dir to use
        handler = MimirHandler()
        handler._init()

        handler._delete()

        assert os.path.exists(mimir_dir) is False

    def test_add_new_note(self):
        working_dir = os.getcwd()
        mimir_dir = working_dir + '/.mimir'
        mimir_notes_file = mimir_dir + '/mimir_notes.txt'

        # First, remove any existing mimir dirs
        if os.path.exists(mimir_dir):
            shutil.rmtree(mimir_dir)

        handler = MimirHandler()
        handler._init()
        kwargs = {'note': ('This', 'is', 'a', 'note.')}
        handler._new(**kwargs)

        with open(mimir_notes_file, 'r') as f:
            lines = f.readlines()

        written_note = lines[2].split('::')[1]
        assert ' This is a note.' == written_note

    def test_add_new_single_word_note(self):
        working_dir = os.getcwd()
        mimir_dir = working_dir + '/.mimir'
        mimir_notes_file = mimir_dir + '/mimir_notes.txt'

        # First, remove any existing mimir dirs
        if os.path.exists(mimir_dir):
            shutil.rmtree(mimir_dir)

        handler = MimirHandler()
        handler._init()
        kwargs = {'note': 'testing'}
        handler._new(**kwargs)

        with open(mimir_notes_file, 'r') as f:
            lines = f.readlines()

        written_note = lines[2].split('::')[1]
        assert ' testing' == written_note
