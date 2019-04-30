import click
from greenberet.cli import pass_context

#####
## Cluster functions for Green Beret
#

@click.group()
@pass_context
def cli():
    pass

@click.command()
def list():
    print('List Configured clusters')

@click.command()
def config():
    print('Configure a new cluster')

cli.add_command(list)
cli.add_command(config)


