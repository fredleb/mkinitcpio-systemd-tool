#!/usr/bin/env python

#
# verification script
#

import os
import sys
import time

this_dir = os.path.dirname(os.path.abspath(__file__))

# import shared config
project_root = os.popen("git rev-parse --show-toplevel").read().strip()
python_module = f"{project_root}/tool/module"
sys.path.insert(0, python_module)
from arkon_config import base_machine
from machine_unit import MachineUnit

machine = MachineUnit(base_machine, this_dir)

machine.perform_make_boot()
