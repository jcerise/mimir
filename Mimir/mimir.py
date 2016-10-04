import click
from enum import Enum

from Mimir.mimir_handler import MimirHandler


class Actions(Enum):
    init = 1
    delete = 2


@click.command()
@click.argument('action')
def cli(action=None):
    actions = Actions
    handler = MimirHandler()
    try:
        if action in actions.__members__:
            if action == 'delete':
                if click.confirm('Are you sure you wish to delete any mimirs found?'):
                    handler.handle(action)
            else:
                handler.handle(action)
        else:
            raise KeyError('Action not found!')
    except KeyError as ex:
        print 'Invalid action supplied'

        valid = ''
        for action in actions:
            valid += action.name + ' '

        print 'Valid actions: {}'.format(valid)
        print 'Run \'mimir --help\' for more information'

