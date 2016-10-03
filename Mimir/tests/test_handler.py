import os

import shutil
from mock import patch

from Mimir.mimir import Actions
from Mimir.mimir_handler import MimirHandler


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
