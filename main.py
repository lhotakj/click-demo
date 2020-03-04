# colors https://misc.flogisoft.com/bash/tip_colors_and_formatting
import click


@click.group()
def group_create():
    pass


@group_create.command(
    help='\033[38;5;133mCreates instance\033[0m - Creates a new instance according the precept with optional override parameters')
@click.option('--precept', '-p', required=True, default=None, help='\033[96mName of the precept\033[0m', type=str,
              metavar="\033[32m<precept>\033[0m")
@click.option('--force-recreate', '-f', required=False, default=False, is_flag=True,
              help='\033[38;5;73mIn case if the instance already exists it will shut it down\033[0m')
@click.option('--name', '-n', required=False, default=None,
              help='\033[38;5;73mOptional name of the instance, if not defined it\'s taken from the precept\033[0m',
              type=str,
              metavar="\033[32m<instance-id>\033[0m")
@click.option('--wait', '-w', default=False, is_flag=True,
              help='\033[38;5;73mWaits until operation completes, by default it sends the signal and exits\033[0m')
@click.option('--verbose', '-v', required=False, default=False, is_flag=True,
              help='\033[38;5;73mShow debug info\033[0m')
@click.help_option('--help', '-h', help='\033[38;5;73mShows this message and exits\033[0m')
def create(precept: str, force_recreate: bool, name: str, wait: bool, verbose: bool):
    print(f'creating new instance with name:{name} according precept:{precept}, wait:{wait}, verbose:{verbose}')


@click.group()
def group_stop():
    pass


@group_stop.command(
    help='\033[38;5;134mStops an instance\033[0m - Sends a signal to AWS to stop instance \033[32m<instance-id>\033[0m')
@click.argument('instance-id', required=True, default=None, type=str, metavar="\033[32m<instance-id>\033[0m")
@click.option('--wait', '-w', default=False, is_flag=True,
              help='\033[38;5;73mWaits until operation completes, by default it sends the signal and exits\033[0m')
@click.option('--verbose', '-v', required=False, default=False, is_flag=True,
              help='\033[38;5;73mShow debug info\033[0m')
@click.help_option('--help', '-h', help='\033[38;5;73mShows this message and exits\033[0m')
def stop(instance_id: str, wait: bool, verbose: bool):
    print(f'stopping an instance {instance_id} with verbose:{verbose} and wait:{wait}')


@click.group()
def group_terminate():
    pass


@group_terminate.command(
    help='\033[38;5;135mTerminates an instance\033[0m - Sends a signal to AWS to terminate instance \033[32m<instance-id>\033[0m')
@click.argument('instance-id', required=True, default=None, type=str, metavar="\033[32m<instance-id>\033[0m")
@click.option('--wait', '-w', default=False, is_flag=True,
              help='\033[38;5;73mWaits until operation completes, by default it sends the signal and exits\033[0m')
@click.option('--verbose', '-v', required=False, default=False, is_flag=True,
              help='\033[38;5;73mShow debug info\033[0m')
@click.help_option('--help', '-h', help='\033[38;5;73mShows this message and exits\033[0m')
def terminate(instance_id: str, wait: bool, verbose: bool):
    print(f'terminating an instance {instance_id} with verbose:{verbose} and wait:{wait}')


@click.command(cls=click.CommandCollection, sources=[group_create, group_stop, group_terminate],
               context_settings=dict(max_content_width=150))
@click.help_option(help='\033[38;5;71mShows this message and exits\033[0m')
@click.version_option(help='\033[38;5;72mShow version info and exists\033[0m')
def cli():
    pass


if __name__ == '__main__':
    cli()
