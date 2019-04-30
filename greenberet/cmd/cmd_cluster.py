import click
from greenberet.cli import pass_context

#####
## Cluster functions for Green Beret
#

@click.group(help='Commands for setting up cluster connections')
@pass_context
def cli():
    pass

@click.command(help='list all the configured clusters')
def list():
    print('list configured clusters')

@click.command(help='setup a new cluster connection')
def config():
    print('configure a new cluster')

cli.add_command(list)
cli.add_command(config)


