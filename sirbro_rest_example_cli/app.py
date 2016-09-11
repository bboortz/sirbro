#!/usr/bin/env python3

import os
import sys

from sirbro_app import __projname__, __projver__, __projdesc__, __apiversions__
from sirbro_app.app import *
from sirbro_lib import __projname__ as __libname__, __projver__ as __libver__
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
parser.add_argument('-V', '--version', action='version', version='%(prog)s {version} - apiversions: {apiversions}'.format(version=__projver__, apiversions=__apiversions__))
subparsers = parser.add_subparsers(dest="subparser_name") 
api_parser = subparsers.add_parser('api', help='api info')
api_group = api_parser.add_mutually_exclusive_group(required=True)
api_group.add_argument('-a', '--alive', action='store_true', help='get api alive status')
api_group.add_argument('-i', '--info', action='store_true', help='get api info')
api_group.add_argument('-c', '--config', action='store_true', help='get api config')
resource_parser = subparsers.add_parser('resource', help='manage a resource')
resource_group = resource_parser.add_mutually_exclusive_group(required=True)
resource_group.add_argument('-c', '--create', action='store_true', help='create the resource')
resource_group.add_argument('-d', '--delete', action='store_true', help='delete the resource')
resource_parser.add_argument('-f', '--file', dest='config_file', help='specify the config file')



#
# * functions*
#
def retrieveArgument(args, key, default=None):
    if key not in args  or  args[key] == None:
        return default
    return args[key]


def exit_with_help():
    parser.print_help()
    sys.exit(1)



#
# * main routine *
#
def main():
    LOGGER.info("%s %s starting..." % (__projname__, __projver__) )
    LOGGER.debug("using %s %s." % (__libname__, __libver__) )
    LOGGER.info("BASE_URL is %s." % (AppConfig.BASE_URL) )

    # parse the arguments
    if len(sys.argv)==1:
        exit_with_help()

    args = vars( parser.parse_args() )
    LOGGER.debug(args)

    if 'subparser_name' not in args:
        exit_with_help
    subparser_name = args['subparser_name']




    # parse the subparser / commands
    try:
        if subparser_name == 'api':
            if args['alive']:
                api_get_alive()
            elif args['info']:
                api_get_info()
            elif args['config']:
                api_get_config()
            else:
                exit_with_help()
            
        elif subparser_name == 'resource':
                LOGGER.info("resource")
        else:
            parser.print_help()
            sys.exit(1)

    except KeyboardInterrupt:
        LOGGER.info("^C")

    LOGGER.info("%s %s stopped." % (__projname__, __projver__) )

if __name__ == "__main__":
    main()
