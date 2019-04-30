import click
from greenberet.cli import pass_context

#####
## Project functions for Green Beret
#

@click.group()
@pass_context
def cli():
    pass

@click.command()
def list():
    print('List Projects')

@click.command()
def create():
    print('Create a new project')

cli.add_command(list)
cli.add_command(create)

