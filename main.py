import click


@click.group()
def group_create():
    pass


@group_create.command(help='\033[38;5;133mCreates instance\033[0m')
@click.option('--name', '-n', required=True, default=None, help='name of the instance', type=str)
def create(name: str):
    """\033[92mCreates\033[0m an EC2 instance"""
    print(f'creating new instance {name}')


@click.group()
def group_stop():
    pass


@group_stop.command(help='\033[38;5;134mStops an instance\033[0m')
@click.option('--instance-id', '-i', required=True, default=None, help='\033[32mid of the instance\033[0m', type=str)
def stop(name: str):
    """\033[92mCreates\033[0m an EC2 instance"""
    print(f'creating new instance {name}')


@click.group()
def group_terminate():
    pass


@group_terminate.command(help='\033[38;5;135mTerminates an instance\033[0m')
@click.option('--instance-id', '-i', required=True, default=None, help='\033[32mid of the instance\033[0m', type=str)
def terminate(instance_id: str):
    """\033[92mTerminates\033[0m an EC2 instance"""
    print(f'terminating new instance {instance_id}')


@click.command(cls=click.CommandCollection, sources=[group_create, group_stop, group_terminate])
@click.help_option(help='\033[38;5;71mshows this message and exits\033[0m')
@click.version_option(help='\033[38;5;72mshow version info\033[0m')
@click.option('--debug', default=False, is_flag=True, help='\033[38;5;73mshow debug info\033[0m')
def cli(debug):
    pass

if __name__ == '__main__':
   cli()
