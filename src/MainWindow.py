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


    def on_ui_auto_shutdown_switch_toggled(self, switch, _):
        is_active = switch.get_active()
        self.ui_auto_shutdown_hour_plus_button.set_sensitive(is_active)
        self.ui_auto_shutdown_hour_minus_button.set_sensitive(is_active)
        self.ui_auto_shutdown_minute_plus_button.set_sensitive(is_active)
        self.ui_auto_shutdown_minute_minus_button.set_sensitive(is_active)

    def on_ui_timed_shutdown_switch_toggled(self, switch, _):
        is_active = switch.get_active()
        self.ui_timed_shutdown_hour_plus_button.set_sensitive(is_active)
        self.ui_timed_shutdown_hour_minus_button.set_sensitive(is_active)
        self.ui_timed_shutdown_minute_plus_button.set_sensitive(is_active)
        self.ui_timed_shutdown_minute_minus_button.set_sensitive(is_active)

    def on_ui_timed_suspend_switch_toggled(self, switch, _):
        is_active = switch.get_active()
        self.ui_timed_suspend_hour_plus_button.set_sensitive(is_active)
        self.ui_timed_suspend_hour_minus_button.set_sensitive(is_active)
        self.ui_timed_suspend_minute_plus_button.set_sensitive(is_active)
        self.ui_timed_suspend_minute_minus_button.set_sensitive(is_active)

    def on_ui_set_status(self):
        if self.ui_auto_shutdown_switch.get_active():
            self.ui_status_label.set_text("Auto shutdown mode active")
        elif self.ui_timed_shutdown_switch.get_active():
            self.ui_status_label.set_text("Timed shutdown mode active")
        elif self.ui_timed_suspend_switch.get_active():
            self.ui_status_label.set_text("Timed suspend mode active")
        else:
            self.ui_status_label.set_text("No settings")
