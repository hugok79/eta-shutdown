import os
import gi
import threading
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

ACTION=os.path.dirname(os.path.abspath(__file__))+"/actions.py"

class ShutdownMenu:
    def __init__(self):
        window = Gtk.Window()
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box.set_spacing(18)
        box.pack_start(self.create_button("gtk-ok", ["pkexec", ACTION, "reboot"]), True, True, 0)
        box.pack_start(self.create_button("gtk-yes", ["pkexec", ACTION, "poweroff"]), True, True, 0)
        box.pack_start(self.create_button("gtk-no", ["pkill","-KILL", "-u", os.environ["USER"]]), True, True, 0)
        window.add(box)
        window.set_resizable(False)
        window.set_decorated(False)
        window.set_keep_above(True)
        window.show_all()

    def create_button(self, icon, command):
        def event(winget):
            subprocess.run(command)
        button = Gtk.Button()
        image = Gtk.Image()
        image.set_from_icon_name(icon, 0)
        image.set_pixel_size(300)
        button.add(image)
        button.connect("clicked", event)
        return button

if __name__ == "__main__":
    menu=ShutdownMenu()
    Gtk.main()
