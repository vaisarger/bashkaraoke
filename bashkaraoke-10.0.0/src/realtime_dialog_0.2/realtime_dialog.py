#!/usr/bin/env python
# *-* coding: utf-8 *-*
#
# realtime_dialog.py
# Copyright (C) 2010-2016 Vittorio Cagnetta <vaisarger@gmail.com>
#                         Davide Depau <david.dep.1996@gmail.com>
#
# EasyBashGUI is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# EasyBashGUI is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.    If not, see <http://www.gnu.org/licenses/>.

import argparse
import os
import sys
import time
import thread


program = "EasyBashGUI (realtime updated dialog)"
version = "4.0.3"

def parseargs():
    parser = argparse.ArgumentParser(description="Reads a file and prints its content in real-time")
    #parser.add_argument("-m", "--mode", default="auto", nargs="?", choices=["auto", "gtk", "qt"], required=False, metavar="TOOLKIT", help="Forces the program to use a custom toolkit")
    parser.add_argument("-i", "--icon", default="emblem-presentation", required=False, help="Sets the icon from icon name or file")
    parser.add_argument("-s", "--size", default="400x400", nargs="?", required=False, metavar="WIDTHxHEIGHT", help="Sets the size of the window. Example: \"400x300\"")
    parser.add_argument("-f", "--fullscreen", default=False, required=False, action="store_true", help="Starts the dialog in fullscreen mode.")
    parser.add_argument("file", metavar="/path/to/file", help="Sets a custom file to be shown.")
    parser.add_argument("-v", '--version', action='version', help="Displays the current version and exits", version='{0} {1}'.format(program, version))
    global args
    args = parser.parse_args()
    if not (os.path.exists(os.path.abspath(args.file)) and os.path.isfile(os.path.abspath(args.file))):
        raise IOError("No such file: {0}".format(args.file))

if __name__ == "__main__":
    try:
        parseargs()
        #auto = False
        #if args.mode == "auto":
        #    auto = True
        #    if os.environ.get("XDG_CURRENT_DESKTOP") == "Unity" or os.environ.get("DESKTOP_SESSION") in ("ubuntu", "gnome-shell"):
        #        args.mode = "gtk"
        #    else:
        #        args.mode = "gtk"
        #count = 0
        #while count < 2:
        #    count += 1
        #    if args.mode == "gtk":
        #        try:
        #            from gi.repository import Gtk, Gdk, GLib
        #            gtk = True
        #            del Gtk, Gdk, GLib
        #            break
        #        except:
        #            if not auto:
        #                raise ImportError("Gtk is not installed. Try to run \"sudo apt-get install gir1.2-glib-2.0 gir1.2-gtk-3.0\"")
        #            else:
        #                gtk = False
        #                args.mode == "qt"
        #    if args.mode == "qt":
        #        try:
        #            from PyQt4 import QtGui, QtCore
        #            qt = True
        #            del QtGui, QtCore
        #            break
        #        except:
        #            if not auto:
        #                raise ImportError("PyQt4 is not installed. Try to run \"sudo apt-get install python-qt4\"")
        #            else:
        #                qt = False
        #                args.mode = "gtk"
        #del count
        #if not gtk and not qt:
        #    raise ImportError("To use the program you need or GTK+ 3 or PyQt4. Neither of them is installed.\nTry to run \"sudo apt-get install gir1.2-glib-2.0 gir1.2-gtk-3.0 python-qt4\"")
        #args.mode = "gtk" # I set GTK because Qt UI is not ready
        #exec "import realtime_dialog_{0} as dialog".format(args.mode)
        import realtime_dialog_gtk as dialog
        #if auto:
        #    args.mode = "auto"

        dialog.init(args)

    except KeyboardInterrupt:
        pass

