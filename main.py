#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from random import randint
from config import SEED
from view.gui import Launcher


SEED = randint(1000, 2000)


if len(sys.argv) > 1:
    Launcher(sys.argv[1])
else:
    Launcher('')
