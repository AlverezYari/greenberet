import click
from greenberet.cli import pass_context

#####
## Project functions for Green Beret
#

@click.group(help='Commands for interacting with Brigade Projects')
@pass_context
def cli():
    pass

@click.command()
def list(help='list projects deployed on selected cluster'):
    print('List Projects')

@click.command()
def create(help='sets up a new project on the selected cluster'):
    print('Create a new project')

cli.add_command(list)
cli.add_command(create)

