#!/usr/bin/env python

import os
import sys
from logics.Search import *

if __name__ == "__main__":

    search_inv_init()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SearchEngine.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
