import click
from greenberet.cli import pass_context

#####
## Build functions for Green Beret
#

@click.group(help='Commands for interacting with Brigade Builds')
@pass_context
def cli():
    pass

@click.command(help='list builds')
def list():
    print('list builds from selected cluster')

@click.command(help='get a build')
def get():
    print('get a build from selected cluster')

@click.command(help='deletes a build')
def delete():
    print('deletes a build from selected cluster')

@click.command(help='deletes all builds for a project')
def delete_all():
    print('deletes all builds for a project on selected cluster')

@click.command(help='show build logs')
def logs():
    print('show build logs')


cli.add_command(list)
cli.add_command(get)
cli.add_command(delete)
cli.add_command(delete_all, name='delete-all')
cli.add_command(logs)


