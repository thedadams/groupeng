#!/usr/bin/python

# Copyright 2011, Thomas G. Dimiduk
#
# This file is part of GroupEng.
#
# Holopy is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Holopy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with GroupEng.  If not, see <http://www.gnu.org/licenses/>.

import controller
import sys
from Tkinter import *
from tkFileDialog import askopenfilename
from tkMessageBox import showerror
import os.path
import os

if len(sys.argv) > 1:
#    try:
        groups, status = controller.run(sys.argv[1])
        if not status:
            print('Could not completely meet all rules')
#    except Exception as e:
#        print(e)

else:
    path = askopenfilename()
    d, f = os.path.split(path)
    os.chdir(d)
    try:
        controller.run(f)
    except Exception as e:
        showerror('Error', '{0}'.format(e))