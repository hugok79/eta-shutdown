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
        self.ui_shutdown_board_switch = UI("ui_shutdown_board_switch")
        
        # time boxes
        self.ui_auto_shutdown_time_box = UI("ui_auto_shutdown_time_box")
        self.ui_shutdown_board_time_box = UI("ui_shutdown_board_time_box")
        self.ui_auto_shutdown_hour_box = UI("ui_auto_shutdown_hour_box")
        self.ui_auto_shutdown_minute_box = UI("ui_auto_shutdown_minute_box")
        self.ui_shutdown_board_hour_box = UI("ui_shutdown_board_hour_box")
        self.ui_shutdown_board_minute_box = UI("ui_shutdown_board_minute_box")
        
        # plus/minues buttons
        self.ui_auto_shutdown_hour_plus_button = UI("ui_auto_shutdown_hour_plus_button")
        self.ui_auto_shutdown_hour_minus_button = UI("ui_auto_shutdown_hour_minus_button")
        self.ui_auto_shutdown_minute_plus_button = UI("ui_auto_shutdown_minute_plus_button")
        self.ui_auto_shutdown_minute_minus_button = UI("ui_auto_shutdown_minute_minus_button")
        self.ui_shutdown_board_hour_plus_button = UI("ui_shutdown_board_hour_plus_button")
        self.ui_shutdown_board_hour_minus_button = UI("ui_shutdown_board_hour_minus_button")
        self.ui_shutdown_board_minute_plus_button = UI("ui_shutdown_board_minute_plus_button")
        self.ui_shutdown_board_minute_minus_button = UI("ui_shutdown_board_minute_minus_button")

        # labels
        self.ui_auto_shutdown_hour_label = UI("ui_auto_shutdown_hour_label")
        self.ui_auto_shutdown_minute_label = UI("ui_auto_shutdown_minute_label")
        self.ui_shutdown_board_hour_label = UI("ui_shutdown_board_hour_label")
        self.ui_shutdown_board_minute_label = UI("ui_shutdown_board_minute_label")
        self.ui_status_label = UI("ui_status_label")

        # buttons
        self.ui_save_button = UI("ui_save_button")

    def define_variables(self):
        #self.ui_status_label.set_text("Hello Pardus!")
        pass

    def on_ui_save_button_clicked(self, button):
        self.ui_status_label.set_text("Hello Pardus!")
