# click-demo


A simple demo of usage `click` module
- colored help
- using commands
- custom help option
- custom common options by a wraper of decorators

usage: 
```
$ python3 ./main.py --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help     Shows this message and exits
  --version  Show version info and exists

Commands:
  create     Creates instance - Creates a new instance according the precept with optional override parameters
  stop       Stops an instance - Sends a signal to AWS to stop instance <instance-id>
  terminate  Terminates an instance - Sends a signal to AWS to terminate instance <instance-id>
```

or specificaly for command `start`:
Note that last (`wait`, `verbose` `quiet` `dryrun` and `help` commands are defined in @common_options
```
$ python3 ./main.py create --help
Usage: main.py create [OPTIONS]

  Creates instance - Creates a new instance according the precept with optional override parameters

Options:
  -p, --precept <precept>     Name of the precept  [required]
  -t, --type <instance-type>  Optional type of the instance, if not defined it's taken from the precept. Visit
                              https://aws.amazon.com/ec2/instance-types/ for the complete list of AWS EC2 instance types
  -f, --force-recreate        In case if the instance already exists it will shut it down
  -n, --name <instance-id>    Optional name of the instance, if not defined it's taken from the precept
  -w, --wait                  Waits until operation completes, by default it sends the signal and exits
  -v, --verbose               Show debug info
  -q, --quiet                 Quiet mode, suppress any errors or warnings except the desired output. That includes even this help.                                                                                                
  -d, --dryrun                Runs in dry run mode                                                                                                                                                                                
  -h, --help                  Shows this message and exits   
  
```
