import click

@click.group()
@click.option('--version', help="Prints your green beret version number")
@click.pass_context
def main (ctx,version):
    '''
    Green Beret the Python Brigade Client
    '''
    # null:click.echo('Main CLI')
    pass

# Cluster Commands

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

# Project Commands

@main.command()
@click.option('-l','--list',  help='List project deployed in your target cluster', is_flag=True)
@click.option('-g','--get', help='Get a specific project by id', type=str)
@click.option('-c', '--create', help="Create a new project", )
@click.option('-d','--delete', help='Deletes project from cluster', type=str)
@click.pass_context
def project(ctx,list,get,create,delete):
    '''
    Project Functions 
    '''
    if list:
        #Call list function
        click.echo('List Projects')
    elif get != None:
        #call get function
        click.echo('Get Projects')
    elif create != None:
        #call Create function
        click.echo('Create a new project')
    elif delete != None:
        #call Delete function
        click.echo('Delete a project')
    pass


def start():
    main(obj={})


if __name__ == "__main__":
    start()

