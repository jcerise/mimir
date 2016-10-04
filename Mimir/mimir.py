import click
from enum import Enum

from Mimir.mimir_handler import MimirHandler


class Actions(Enum):
    init = 1
    delete = 2
    new = 3


@click.command()
@click.argument('action', nargs=-1)
def cli(action=None):
    actions = Actions
    handler = MimirHandler()

    # TODO: What about one word notes? Should we just fall through when an action isn't found?
    if len(action) == 1:
        action = action[0]
        try:
            if action in actions.__members__:
                if action == 'delete':
                    if click.confirm('Are you sure you wish to delete any mimirs found?'):
                        handler.handle(action)
                else:
                    handler.handle(action)
            else:
                raise KeyError('Action not defined!')
        except KeyError as ex:
            print 'Invalid action supplied'

            valid = ''
            for action in actions:
                valid += action.name + ' '

            print 'Valid actions: {}'.format(valid)
            print 'Run \'mimir --help\' for more information'
    else:
        # If multiple arguments were passed in, assume no specific action, and create a note instead.
        handler.handle('new')

