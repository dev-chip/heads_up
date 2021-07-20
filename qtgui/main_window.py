# -------------------------------------------------------------------------------
# Name:        main_window.py
# Purpose:     Main window example.
#
# Author:      James Cook
#
# Created:     30/09/2020
# Copyright:   (c) James Cook 2020
# -------------------------------------------------------------------------------

# native modules
from PyQt5.QtGui import (QColor,
                         QFont)
from PyQt5.QtWidgets import (QTableWidgetItem,
                             QDialog)

# project modules
from qtgui.gen import MainWindowGenerated
from qtgui.window import Window
from qtgui.logger import init_console_logger
from qtgui.show_dialog import show_message_dialog
from qtgui.workers.calendar_worker import GetCalendar
from qtgui.gen import CreateShortcutDialogGenerated as ShortcutDialog

from datetime import datetime, timedelta
import re


logger = init_console_logger(name="gui")


class MainWindow(Window):

    def __init__(self):

        logger.debug("Setting up UI")
        super(Window, self).__init__()
        self.ui = MainWindowGenerated.Ui_MainWindow()
        self.ui.setupUi(self)

        logger.verbose("Initialising GUI logger")
        self.init_GUI_logger(logger)

        logger.verbose("Initialising signals")
        self.init_signals()

        self.ui.plainTextEdit_today.setPlainText("")
        self.ui.plainTextEdit_tomorrow.setPlainText("")
        self.ui.label_today_title.setText("...")
        self.ui.label_tomorrow_title.setText("...")

        self.start_calendar_update_thread(calendar_days=28, update_frequency=30)
        self.load_shortcuts()

        logger.info("GUI initialised")

    def init_signals(self):
        """
            Initialises widget signals
        """
        self.ui.action_manage_shortcuts.triggered.connect(self.show_add_shortcut_dialog)

    def start_calendar_update_thread(self, calendar_days, update_frequency):
        assert calendar_days > 0
        assert update_frequency > 0
        assert type(calendar_days) == int

        logger.debug("Starting GetCalendar thread...")
        t = GetCalendar(success_callback=self.update_calendars,
                        error_callback=self.error_updating_calendar,
                        calendar_days=calendar_days,
                        update_frequency=update_frequency)
        t.start()
        logger.debug("GetCalendar thread started")

    def error_updating_calendar(self, e):
        logger.error("Calendar thread error:" + str(e))
        show_message_dialog("A error with the calendar updater occurred. "
                            "Try restarting the application to fix this issue.")
        self.ui.plainTextEdit_today.setEnabled(False)
        self.ui.plainTextEdit_tomorrow.setEnabled(False)
        self.ui.tableWidget_calendar.setEnabled(False)
        self.ui.action_refresh_calendars.setEnabled(False)

    def show_add_shortcut_dialog(self):
        dialog = QDialog()
        self.sd_interface = ShortcutDialog.Ui_Dialog()
        self.sd_interface.setupUi(dialog)
        self.sd_interface.buttonGroup.buttonClicked.connect(self.shortcut_dialog_radio_button_selected)
        if dialog.exec_() == 1:
            print("wooo")
            return True
        return False

    def shortcut_dialog_radio_button_selected(self):
        # hack to get around weird QT button id assignment (counts down from -2)
        button_id = (self.sd_interface.buttonGroup.checkedId() * -1) - 2
        # tab selection
        self.sd_interface.tabWidget.setCurrentIndex(button_id)

    def update_calendars(self, calendar_days, appts_today, appts_tomorrow, appts_calendar):
        s = ""
        for a in appts_today:
            if not (a.start_time == '00:00' and a.end_time == '00:00'):  # all-day event
                s += a.start_time + ' - ' + a.end_time + '\t'
            s += a.subject + '\n'
        self.ui.plainTextEdit_today.setPlainText(s)

        s = ""
        for a in appts_tomorrow:
            if not (a.start_time == '00:00' and a.end_time == '00:00'):  # all-day event
                s += a.start_time + ' - ' + a.end_time + '\t'
            s += a.subject + '\n'
        self.ui.plainTextEdit_tomorrow.setPlainText(s)

        dates_list = [[datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=i), "Office"] for i in range(calendar_days)]

        i = 0
        while i < len(dates_list):
            if dates_list[i][0].weekday() > 4:
                dates_list[i][1] = "Leave"
            i += 1

        for a in appts_calendar:
            i = 0
            while i < len(dates_list):
                if dates_list[i][0].date() == a.date.date():

                    if (re.findall(r'^vacation', a.subject, re.IGNORECASE) or
                            re.findall(r'out.+of.+office', a.subject, re.IGNORECASE) or
                            re.findall(r'annual.+leave', a.subject, re.IGNORECASE)):
                        dates_list[i][1] = "Leave"

                    elif re.findall(r'home.+office', a.subject, re.IGNORECASE):
                        dates_list[i][1] = "H.Office"

                    break
                i += 1

        offset = datetime.today().weekday()
        colors = {"Leave": QColor(24, 217, 72),
                  "H.Office": QColor(138, 212, 255),
                  "Office": QColor(24, 146, 217)}

        # set titles
        first_monday = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=offset)
        for x in range(calendar_days//7):
            table_widget_item = QTableWidgetItem((first_monday + timedelta(days=x*7)).strftime("%d/%m"))
            #font = QFont()
            #font.setBold(True)
            #table_widget_item.setFont(font)
            self.ui.tableWidget_calendar.setItem(x+1, 0, table_widget_item)

        # set data
        for x in range(calendar_days//7):
            for y in range(7):
                if x == 0 and y < offset:
                    continue
                self.ui.tableWidget_calendar.setItem(x+1, y+1, QTableWidgetItem(dates_list[(x*7)+y-offset][1]))
                self.ui.tableWidget_calendar.item(x+1, y+1).setBackground(colors[dates_list[(x*7)+y-offset][1]])
                if (x*7)+y-offset == 0:
                    font = QFont()
                    font.setBold(True)
                    font.setUnderline(True)
                    self.ui.tableWidget_calendar.item(x+1, y+1).setFont(font)

        self.ui.label_today_title.setText(datetime.today().strftime('%A %d %B'))
        self.ui.label_tomorrow_title.setText((datetime.today() + timedelta(days=1)).strftime('%A %d %B'))

    def load_shortcuts(self):
        pass

    def start_thread_updater(self):
        """
            Starts a thread that updates the elapsed time.
        """
        # start thread
        #logger.debug("Starting thread...")
        # = LoadThread(self.log_thread_callback, self.progress_thread_callback)
        #t.start()
        logger.info("Thread started")


if __name__ == "__main__":
    print ("No module test implemented.")