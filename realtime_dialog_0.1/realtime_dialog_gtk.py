#!/usr/bin/env python
# *-* coding: utf-8 *-*
#
# realtime_dialog_gtk.py
# Copyright (C) 2010-2013 Vittorio Cagnetta <vaisarger@gmail.com>
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

import os, sys, time
from gi.repository import Gtk, Gdk, GLib, WebKit

### MODIFICA QUI ###

# Intervallo di tempo tra un aggiornamento e l'altro
# (l'ho impostato a 5 secondi perché ci mette molto a caricare
# JQuery e l'altro script per l'adattamento. Dovrò vedere di risolvere
# questo problema diversamente).
TIMEOUT = 5000 # (millisecondi)

### MODIFICA QUI ###

class Dialog(object):
    def __init__(self, args):
        self.args = args
        self.filename = os.path.abspath(os.path.expanduser(self.args.file))

        self.builder = Gtk.Builder()
        self.builder.add_from_file("dialog.ui")
        self.builder.connect_signals(self)
        self.main = self.builder.get_object("window")
        self.scrolledwindow = self.builder.get_object("scrolledwindow")
        self.tb_fullscreen = self.builder.get_object("tb_fullscreen")
        self.webview = WebKit.WebView()
        self.scrolledwindow.add(self.webview)
        self.webview.connect("title-changed", self.title_changed)
        self.webview.load_uri("file://" + self.filename)

        self.is_fullscreen = False
        if self.args.fullscreen:
            self.on_fullscreen()
        if os.path.exists(os.path.abspath(self.args.icon)) and os.path.isfile(os.path.abspath(self.args.icon)):
            try: self.main.set_icon_from_file(os.path.abspath(self.args.icon))
            except: pass
        else:
            try: self.main.set_icon_name(self.args.icon)
            except: pass
        self.size = self.args.size.split("x")
        for x in self.size:
            x = int(x)
        try:
            self.main.set_size(int(self.size[0]), int(self.size[1]))
        except: pass
        self.main.show_all()

        self.wait_gtk()
        GLib.timeout_add(TIMEOUT, self.refresh_label)

    def on_fullscreen(self, widget=None):
        if not self.is_fullscreen:
            self.main.fullscreen()
            self.tb_fullscreen.set_stock_id(Gtk.STOCK_LEAVE_FULLSCREEN)
            self.tb_fullscreen.set_label("Exit fullscreen")
            self.is_fullscreen = True
        elif self.is_fullscreen:
            self.main.unfullscreen()
            self.tb_fullscreen.set_stock_id(Gtk.STOCK_FULLSCREEN)
            self.tb_fullscreen.set_label("Fullscreen")
            self.is_fullscreen = False

    def refresh_label(self):
        self.webview.reload()
        return True

    def title_changed(self, webview, frame, title):
        self.main.set_title(title)

    def wait_gtk(self):
        while Gtk.events_pending():
            Gtk.main_iteration()

    def __empty_method(self, arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    def destroy(self, something=None):
        Gtk.main_quit()
        
def init(args):
    app = Dialog(args)
    GLib.threads_init()
    Gdk.threads_init()
    Gdk.threads_enter()
    Gtk.main()
    Gdk.threads_leave()

