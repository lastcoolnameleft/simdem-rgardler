#!/usr/bin/env python3

# This is a python script that emulates a terminal session and runs
# commands from a supplied markdown file..

import optparse
import os
import sys
import time

from cli import Ui
from web import WebUi
import config
from demo import Demo
from environment import Environment

def main():
    """SimDem CLI interpreter"""

    commands = config.modes
    command_string = ""
    for command in commands:
        command_string = command_string + command + "|"
    command_string = command_string[0:len(command_string)-1]
    
    p = optparse.OptionParser("%prog [" + command_string + "] <options> DEMO_NAME", version=config.SIMDEM_VERSION)
    p.add_option('--style', '-s', default="tutorial",
                 help="The style of simulation you want to run. 'tutorial' (the default) will print out all text and pause for user input before running commands. 'simulate' will not print out the text but will still pause for input.")
    p.add_option('--path', '-p', default="demo_scripts/",
                 help="The Path to the demo scripts directory.")
    p.add_option('--auto', '-a', default="False",
                 help="Set to 'true' (or 'yes') to prevent the application waiting for user keypresses between commands. Set to 'no' when running in test mode to allow users to step through each test.")
    p.add_option('--test', '-t', default="False",
                 help="If set to anything other than False the output of the command will be compared to the expected results in the sript. Any failures will be reported")
    p.add_option('--fastfail', default="True",
                 help="If set to anything other than True test execution has will stop on the first failure. This has no affect if running in any mode other than 'test'.")
    p.add_option('--webui', '-w', default="False",
                 help="If set to anything other than False will interact with the user through a Web UI rather than the CLI.")

    options, arguments = p.parse_args()

    if not options.path.endswith("/"):
        options.path += "/"

    if options.auto == "False":
        is_automatic = False
    else:
        is_automatic = True

    if options.test == "False":
        is_test = False
    else:
        is_test = True

    if options.fastfail == "True":
        is_fast_fail= True
    else:
        is_fast_fail= False
        
    if options.style == "simulate":
        simulate = True
    elif options.style == 'tutorial':
        simulate = False
    else:
        print("Unknown style (--style, -s): " + options.style)
        exit(1)

    if len(arguments) == 2:
        script_dir = options.path + arguments[1]
    else:
        script_dir = options.path
        
    filename = "script.md"
    is_docker = os.path.isfile('/.dockerenv')
    demo = Demo(is_docker, script_dir, filename, simulate, is_automatic, is_test);

    cmd = None
    if options.webui == "False":
        ui = Ui()
        if len(arguments) > 0:
            cmd = arguments[0]
            # 'run' is deprecated in the CLI, but not yet removed from code
            if cmd == "tutorial":
                cmd = "run"
    else:
        ui = WebUi()
        while not ui.ready:
            time.sleep(0.25)
            print("Waiting for client connection")
        cmd = None

    demo.set_ui(ui)
    demo.run(cmd)
    
main()
