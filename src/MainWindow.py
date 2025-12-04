import configparser
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio, Gtk

import locale
from locale import gettext as _

# Translation Constants:
APPNAME = "eta-session-operations"
TRANSLATIONS_PATH = "/usr/share/locale"

# Translation functions:
locale.bindtextdomain(APPNAME, TRANSLATIONS_PATH)
locale.textdomain(APPNAME)

CONFIG_FILE = "/etc/pardus/eta-shutdown.conf"

class MainWindow:
    def __init__(self, application):
        # Gtk Builder
        self.builder = Gtk.Builder()

        # Translate things on glade:
        self.builder.set_translation_domain(APPNAME)

        # Import UI file:
        self.builder.add_from_file(os.path.dirname(os.path.abspath(__file__)) + "/../ui/MainWindow.glade")
        self.builder.connect_signals(self)

        # Window
        self.window = self.builder.get_object("ui_main_window")
        self.window.set_application(application)

        # Set application:
        self.application = application

        # Global Definings
        self.define_components()
        self.define_variables()

        # Show Screen:
        self.window.show_all()

    def define_components(self):
        def UI(str):
            return self.builder.get_object(str)
        
        # switches
        self.ui_auto_shutdown_switch = UI("ui_auto_shutdown_switch")
        self.ui_timed_shutdown_switch = UI("ui_timed_shutdown_switch")
        self.ui_timed_suspend_switch = UI("ui_timed_suspend_switch")
        
        # time boxes
        self.ui_auto_shutdown_time_box = UI("ui_auto_shutdown_time_box")
        self.ui_timed_shutdown_time_box = UI("ui_timed_shutdown_time_box")
        self.ui_timed_suspend_time_box = UI("ui_timed_suspend_time_box")
        self.ui_auto_shutdown_hour_box = UI("ui_auto_shutdown_hour_box")
        self.ui_auto_shutdown_minute_box = UI("ui_auto_shutdown_minute_box")
        self.ui_timed_shutdown_hour_box = UI("ui_timed_shutdown_hour_box")
        self.ui_timed_shutdown_minute_box = UI("ui_timed_shutdown_minute_box")
        self.ui_timed_suspend_hour_box = UI("ui_timed_suspend_hour_box")
        self.ui_timed_suspend_minute_box = UI("ui_timed_suspend_minute_box")

        # plus/minues buttons
        self.ui_auto_shutdown_hour_plus_button = UI("ui_auto_shutdown_hour_plus_button")
        self.ui_auto_shutdown_hour_minus_button = UI("ui_auto_shutdown_hour_minus_button")
        self.ui_auto_shutdown_minute_plus_button = UI("ui_auto_shutdown_minute_plus_button")
        self.ui_auto_shutdown_minute_minus_button = UI("ui_auto_shutdown_minute_minus_button")
        self.ui_timed_shutdown_hour_plus_button = UI("ui_timed_shutdown_hour_plus_button")
        self.ui_timed_shutdown_hour_minus_button = UI("ui_timed_shutdown_hour_minus_button")
        self.ui_timed_shutdown_minute_plus_button = UI("ui_timed_shutdown_minute_plus_button")
        self.ui_timed_shutdown_minute_minus_button = UI("ui_timed_shutdown_minute_minus_button")
        self.ui_timed_suspend_hour_plus_button = UI("ui_timed_suspend_hour_plus_button")
        self.ui_timed_suspend_hour_minus_button = UI("ui_timed_suspend_hour_minus_button")
        self.ui_timed_suspend_minute_plus_button = UI("ui_timed_suspend_minute_plus_button")
        self.ui_timed_suspend_minute_minus_button = UI("ui_timed_suspend_minute_minus_button")

        # labels
        self.ui_auto_shutdown_hour_label = UI("ui_auto_shutdown_hour_label")
        self.ui_auto_shutdown_minute_label = UI("ui_auto_shutdown_minute_label")
        self.ui_timed_shutdown_hour_label = UI("ui_timed_shutdown_hour_label")
        self.ui_timed_shutdown_minute_label = UI("ui_timed_shutdown_minute_label")
        self.ui_timed_suspend_hour_label = UI("ui_timed_suspend_hour_label")
        self.ui_timed_suspend_minute_label = UI("ui_timed_suspend_minute_label")
        self.ui_status_label = UI("ui_status_label")

        # buttons
        self.ui_save_button = UI("ui_save_button")

    def define_variables(self):
        # plus/minues buttons
        self.ui_auto_shutdown_hour_plus_button.connect("clicked", lambda w: self.on_ui_increase_hour_button(self.ui_auto_shutdown_hour_label))
        self.ui_auto_shutdown_hour_minus_button.connect("clicked", lambda w: self.on_ui_decrease_hour_button(self.ui_auto_shutdown_hour_label))
        self.ui_auto_shutdown_minute_plus_button.connect("clicked", lambda w: self.on_ui_increase_minute_button(self.ui_auto_shutdown_minute_label))
        self.ui_auto_shutdown_minute_minus_button.connect("clicked", lambda w: self.on_ui_decrease_minute_button(self.ui_auto_shutdown_minute_label))
        self.ui_timed_shutdown_hour_plus_button.connect("clicked", lambda w: self.on_ui_increase_hour_button(self.ui_timed_shutdown_hour_label))
        self.ui_timed_shutdown_hour_minus_button.connect("clicked", lambda w: self.on_ui_decrease_hour_button(self.ui_timed_shutdown_hour_label))
        self.ui_timed_shutdown_minute_plus_button.connect("clicked", lambda w: self.on_ui_increase_minute_button(self.ui_timed_shutdown_minute_label))
        self.ui_timed_shutdown_minute_minus_button.connect("clicked", lambda w: self.on_ui_decrease_minute_button(self.ui_timed_shutdown_minute_label))
        self.ui_timed_suspend_hour_plus_button.connect("clicked", lambda w: self.on_ui_increase_hour_button(self.ui_timed_suspend_hour_label))
        self.ui_timed_suspend_hour_minus_button.connect("clicked", lambda w: self.on_ui_decrease_hour_button(self.ui_timed_suspend_hour_label))
        self.ui_timed_suspend_minute_plus_button.connect("clicked", lambda w: self.on_ui_increase_minute_button(self.ui_timed_suspend_minute_label))
        self.ui_timed_suspend_minute_minus_button.connect("clicked", lambda w: self.on_ui_decrease_minute_button(self.ui_timed_suspend_minute_label))

        self.on_ui_show_settings()

    def on_ui_increase_hour_button(self, label):
        hour = label.get_text()
        hour = int(hour)
        hour = (hour + 1) % 24
        label.set_text(str(hour).zfill(2))

    def on_ui_decrease_hour_button(self, label):
        hour = label.get_text()
        hour = int(hour)
        hour = (hour - 1) % 24
        label.set_text(str(hour).zfill(2))

    def on_ui_increase_minute_button(self, label):
        minute = label.get_text()
        minute = int(minute)
        minute = (minute + 1) % 60
        label.set_text(str(minute).zfill(2))

    def on_ui_decrease_minute_button(self, label):
        minute = label.get_text()
        minute = int(minute)
        minute = (minute - 1) % 60
        label.set_text(str(minute).zfill(2))

    def on_ui_save_button_clicked(self, button):
        #self.ui_status_label.set_text("Hello Pardus!")
        self.on_ui_set_status()
        self.save_eta_shutdown_config()


    def on_ui_auto_shutdown_switch_toggled(self, switch, state):
        is_active = switch.get_active()
        self.ui_auto_shutdown_hour_plus_button.set_sensitive(is_active)
        self.ui_auto_shutdown_hour_minus_button.set_sensitive(is_active)
        self.ui_auto_shutdown_minute_plus_button.set_sensitive(is_active)
        self.ui_auto_shutdown_minute_minus_button.set_sensitive(is_active)

        if state:
            self.ui_timed_suspend_switch.set_active(False)
            self.ui_timed_shutdown_switch.set_active(False)

    def on_ui_timed_shutdown_switch_toggled(self, switch, state):
        is_active = switch.get_active()
        self.ui_timed_shutdown_hour_plus_button.set_sensitive(is_active)
        self.ui_timed_shutdown_hour_minus_button.set_sensitive(is_active)
        self.ui_timed_shutdown_minute_plus_button.set_sensitive(is_active)
        self.ui_timed_shutdown_minute_minus_button.set_sensitive(is_active)

        if state:
            self.ui_timed_suspend_switch.set_active(False)
            self.ui_auto_shutdown_switch.set_active(False)

    def on_ui_timed_suspend_switch_toggled(self, switch, state):
        is_active = switch.get_active()
        self.ui_timed_suspend_hour_plus_button.set_sensitive(is_active)
        self.ui_timed_suspend_hour_minus_button.set_sensitive(is_active)
        self.ui_timed_suspend_minute_plus_button.set_sensitive(is_active)
        self.ui_timed_suspend_minute_minus_button.set_sensitive(is_active)

        if state:
            self.ui_auto_shutdown_switch.set_active(False)
            self.ui_timed_shutdown_switch.set_active(False)

    def on_ui_set_status(self):
        if self.ui_auto_shutdown_switch.get_active():
            self.ui_status_label.set_text("Auto shutdown mode active")
        elif self.ui_timed_shutdown_switch.get_active():
            self.ui_status_label.set_text("Timed shutdown mode active")
        elif self.ui_timed_suspend_switch.get_active():
            self.ui_status_label.set_text("Timed suspend mode active")
        else:
            self.ui_status_label.set_text("No settings")

    def load_or_create_eta_shutdown_config(self):
        config = configparser.ConfigParser()

        if not os.path.exists(CONFIG_FILE):
            config["AUTO_SHUTDOWN"] = {
                "enabled": "False",
                "hour": "0",
                "minute": "0"
            }

            config["TIMED_SUSPEND"] = {
                "enabled": "False",
                "hour": "0",
                "minute": "0"
            }

            config["TIMED_SHUTDOWN"] = {
                "enabled": "False",
                "hour": "0",
                "minute": "0"
            }

            with open(CONFIG_FILE, "w") as file:
                config.write(file)

        config.read(CONFIG_FILE)
        return config

    def save_eta_shutdown_config(self):
        config = configparser.ConfigParser()

        config["AUTO_SHUTDOWN"] = {
            "enabled": str(self.ui_auto_shutdown_switch.get_active()),
            "hour": str(self.ui_auto_shutdown_hour_label.get_text()),
            "minute": str(self.ui_auto_shutdown_minute_label.get_text())
        }

        config["TIMED_SUSPEND"] = {
            "enabled": str(self.ui_timed_suspend_switch.get_active()),
            "hour": str(self.ui_timed_suspend_hour_label.get_text()),
            "minute": str(self.ui_timed_suspend_minute_label.get_text())
        }

        config["TIMED_SHUTDOWN"] = {
            "enabled": str(self.ui_timed_shutdown_switch.get_active()),
            "hour": str(self.ui_timed_shutdown_hour_label.get_text()),
            "minute": str(self.ui_timed_shutdown_minute_label.get_text())
        }

        with open(CONFIG_FILE, "w") as file:
            config.write(file)

    def on_ui_show_settings(self):
        config = self.load_or_create_eta_shutdown_config()

        self.ui_auto_shutdown_switch.set_active(config.getboolean("AUTO_SHUTDOWN", "enabled"))
        self.ui_auto_shutdown_hour_label.set_text(config.get("AUTO_SHUTDOWN", "hour"))
        self.ui_auto_shutdown_minute_label.set_text(config.get("AUTO_SHUTDOWN", "minute"))

        self.ui_timed_suspend_switch.set_active(config.getboolean("TIMED_SUSPEND", "enabled"))
        self.ui_timed_suspend_hour_label.set_text(config.get("TIMED_SUSPEND", "hour"))
        self.ui_timed_suspend_minute_label.set_text(config.get("TIMED_SUSPEND", "minute"))

        self.ui_timed_shutdown_switch.set_active(config.getboolean("TIMED_SHUTDOWN", "enabled"))
        self.ui_timed_shutdown_hour_label.set_text(config.get("TIMED_SHUTDOWN", "hour"))
        self.ui_timed_shutdown_minute_label.set_text(config.get("TIMED_SHUTDOWN", "minute"))

        if config.getboolean("AUTO_SHUTDOWN", "enabled"):
            self.ui_status_label.set_text("Auto shutdown mode active")
        elif config.getboolean("TIMED_SUSPEND", "enabled"):
            self.ui_status_label.set_text("Timed shutdown mode active")
        elif config.getboolean("TIMED_SHUTDOWN", "enabled"):
            self.ui_status_label.set_text("Timed suspend mode active")
        else:
            self.ui_status_label.set_text("No settings")