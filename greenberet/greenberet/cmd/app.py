import click
from ruamel.yaml import YAML

@click.group()
@click.pass_context
def main (ctx):
    '''
    Main GB Cli
    '''
    click.echo('Main CLI')
    pass

@main.command()
@click.option('-n','--name',  help='Your cluster name', confirmation_prompt=True)
@click.option('-s', '--server', help="Cluster server address", type=str)
@click.option('-i','--info', help='Displays current cluster connection info', is_flag=True)
@click.pass_context
def cluster(ctx,name,server,info):
    '''
    Cluster Functions 
    '''
    if info:
        clusterinfo = "Cluster name: casey | Cluster Host Name: letmein.azure.aks.com"
        click.echo(clusterinfo)
    else:
        click.echo('No info')




def start():
    main(obj={})


if __name__ == "__main__":
    start()

