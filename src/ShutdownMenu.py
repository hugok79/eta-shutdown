import os
import gi
import threading
import subprocess

import locale
from locale import gettext as _

# Translation Constants:
APPNAME = "eta-shutdown"
TRANSLATIONS_PATH = "/usr/share/locale"

# Translation functions:
locale.bindtextdomain(APPNAME, TRANSLATIONS_PATH)
locale.textdomain(APPNAME)


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

ACTION=os.path.dirname(os.path.abspath(__file__))+"/actions.py"

class ShutdownMenu:
    def __init__(self):
        window = Gtk.Window()
        window.connect("destroy", Gtk.main_quit)
        window.set_skip_taskbar_hint(True)
        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        box_close = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        button_close = Gtk.Button()
        close_image = Gtk.Image()
        close_image.set_from_icon_name("window-close-symbolic", 0)
        close_image.set_pixel_size(32)
        button_close.add(close_image)
        button_close.set_relief(Gtk.ReliefStyle.NONE)
        box_close.pack_start(Gtk.Label(label=_("Eta Power Off")), True, True, 0)
        box_close.pack_start(button_close, False, False, 0)
        button_close.connect("clicked", lambda x: Gtk.main_quit())
        box_main.pack_start(box_close, True, True, 0)


        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box.set_spacing(18)
        box.pack_start(self.create_button("eta-poweroff", _("Power Off"), ["pkexec", ACTION, "reboot"]), True, True, 0)
        box.pack_start(self.create_button("eta-reboot", _("Restart"), ["pkexec", ACTION, "poweroff"]), True, True, 0)
        box.pack_start(self.create_button("eta-logout", _("Log Out"), ["pkill","-KILL", "-u", os.environ["USER"]]), True, True, 0)
        box_main.pack_start(box, True, True, 0)

        window.add(box_main)
        window.set_resizable(False)
        window.set_decorated(False)
        window.set_keep_above(True)
        window.show_all()

    def create_button(self, icon, name, command):
        def event(winget):
            subprocess.run(command)
        button = Gtk.Button()
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        image = Gtk.Image()
        image.set_from_icon_name(icon, 0)
        image.set_pixel_size(300)
        box.add(image)
        label=Gtk.Label()
        label.set_markup("<span font=\"16\">"+name+"</span>")
        box.add(label)
        button.add(box)
        button.connect("clicked", event)
        button.set_relief(Gtk.ReliefStyle.NONE)
        return button

if __name__ == "__main__":
    menu=ShutdownMenu()
    Gtk.main()
