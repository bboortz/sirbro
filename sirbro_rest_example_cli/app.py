#!/usr/bin/env python3

import os
import sys

from sirbro_app import __projname__, __projver__, __projdesc__
from sirbro_app.app import run_app
from sirbro_lib.logger import getLogger

import argparse



#
# * basic configuration *
#
LOGGER = getLogger('argparser')


#
# * parse arguments *
#



# define the parser arguments
parser = argparse.ArgumentParser(prog=__projname__, description=__projdesc__)
parser.add_argument('-V', '--version', action='version', version='%(prog)s {version}'.format(version=__projver__))
subparsers = parser.add_subparsers(dest="subparser_name") # this line changed
apiinfo_parser = subparsers.add_parser('api', help='api info')
apiinfo_parser.add_argument('--alive', help='get api alive status')
apiinfo_parser.add_argument('--info', help='get api info')
apiinfo_parser.add_argument('--config', help='get api config')
resource_parser = subparsers.add_parser('resource', help='manage a resource')
resource_parser.add_argument('-c', '--create', dest='create', help='create the resource')
resource_parser.add_argument('-d', '--delete', dest='delete', help='delete the resource')
resource_parser.add_argument('-f', '--file', dest='config_file', help='specify the config file')
#run_parser.add_argument('CONTAINER', help='the container to run')



# parse the arguments
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

args = vars( parser.parse_args() )
LOGGER.debug(args)

if 'subparser_name' not in args:
    parser.print_help()
    sys.exit(1)
subparser_name = args['subparser_name']


def retrieveArgument(args, key, default=None):
    if key not in args  or  args[key] == None:
        return default
    return args[key]


# parse the subparser / commands
try:
    if subparser_name == 'api':
            LOGGER.info("api")
    elif subparser_name == 'resource':
            LOGGER.info("resource")
    else:
        parser.print_help()
        sys.exit(1)

except KeyboardInterrupt:
    LOGGER.info("^C")



#
# * main routine *
#
def main():
    run_app()

if __name__ == "__main__":
    main()
