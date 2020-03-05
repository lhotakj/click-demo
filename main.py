#!/usr/bin/python3
# colors https://misc.flogisoft.com/bash/tip_colors_and_formatting
import click
from functools import wraps


@click.group()
def group_create():
    pass


# Add the following options --wait | --verbose | --dryrun | --help
def default_options(fn):
    @wraps(fn)
    @click.option('--wait', '-w', default=False, is_flag=True,
                  help='\033[38;5;73mWaits until operation completes, by default it sends the signal and exits\033[0m')
    @click.option('--verbose', '-v', required=False, default=False, is_flag=True,
                  help='\033[38;5;73mShow debug info\033[0m')
    @click.option('--quiet', '-q', required=False, default=False, is_flag=True,
                  help='\033[38;5;73mQuiet mode, suppress any errors or warnings except the desired output. That includes even this help.\033[0m')
    @click.option('--dryrun', '-d', required=False, default=False, is_flag=True,
                  help='\033[38;5;73mRuns in dry run mode\033[0m')
    @click.help_option('--help', '-h', help='\033[38;5;73mShows this message and exits\033[0m')
    def wrapped(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapped


@group_create.command(
    help='\033[38;5;133mCreates instance\033[0m - Creates a new instance according the precept with optional override parameters')
@click.option('--precept', '-p', required=True, default=None, help='\033[96mName of the precept\033[0m', type=str,
              metavar="\033[32m<precept>\033[0m")
@click.option('--type', '-t', required=False, default=None,
              help='\033[38;5;73mOptional type of the instance, if not defined it\'s taken from the precept. Visit https://aws.amazon.com/ec2/instance-types/ for the complete list of AWS EC2 instance types\033[0m',
              type=str,
              metavar="\033[32m<instance-type>\033[0m")
@click.option('--force-recreate', '-f', required=False, default=False, is_flag=True,
              help='\033[38;5;73mIn case if the instance already exists it will shut it down\033[0m')
@click.option('--name', '-n', required=False, default=None,
              help='\033[38;5;73mOptional name of the instance, if not defined it\'s taken from the precept\033[0m',
              type=str,
              metavar="\033[32m<instance-id>\033[0m")
@default_options
def create(precept: str, instance_type: str, force_recreate: bool, name: str, wait: bool, verbose: bool, quiet: bool, dryrun: bool):
    print(f'creating new instance with name:{name} according precept:{precept}, instance-type:{instance_type}, wait:{wait}, verbose:{verbose}, quiet:{quiet}, dryrun:{dryrun}')


@click.group()
def group_stop():
    pass


@group_stop.command(
    help='\033[38;5;134mStops an instance\033[0m - Sends a signal to AWS to stop instance \033[32m<instance-id>\033[0m')
@click.argument('instance-id', required=True, default=None, type=str, metavar="\033[32m<instance-id>\033[0m")
@default_options
def stop(instance_id: str, wait: bool, verbose: bool, quiet: bool, dryrun: bool):
    print(f'stopping an instance {instance_id} with verbose:{verbose} and wait:{wait}, quiet:{quiet}, dryrun:{dryrun}')


@click.group()
def group_terminate():
    pass


@group_terminate.command(
    help='\033[38;5;135mTerminates an instance\033[0m - Sends a signal to AWS to terminate instance \033[32m<instance-id>\033[0m')
@click.argument('instance-id', required=True, default=None, type=str, metavar="\033[32m<instance-id>\033[0m")
@default_options
def terminate(instance_id: str, wait: bool, verbose: bool, quiet: bool, dryrun: bool):
    print(f'terminating an instance {instance_id} with verbose:{verbose} and wait:{wait}, quiet:{quiet}, dryrun:{dryrun}')


@click.command(cls=click.CommandCollection, sources=[group_create, group_stop, group_terminate],
               context_settings=dict(max_content_width=150))
@click.help_option(help='\033[38;5;71mShows this message and exits\033[0m')
@click.version_option(help='\033[38;5;72mShow version info and exists\033[0m')
def cli():
    pass


if __name__ == '__main__':
    cli()
