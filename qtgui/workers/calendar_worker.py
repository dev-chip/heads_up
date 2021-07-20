# -------------------------------------------------------------------------------
# A generic worker thread example
# -------------------------------------------------------------------------------

from time import sleep
import threading

from qtgui.workers.classes import CommunicateSuccess, CommunicateError
#from qtgui.logger import init_signal_logger

from core.calendar import Calendar


class GetCalendar(threading.Thread):
    """
        Gets Outlook calendar events.
    """

    def __init__(self, success_callback, error_callback, calendar_days, update_frequency):
        threading.Thread.__init__(self)

        self.ComSuccess = CommunicateSuccess()
        self.ComSuccess.myGUI_signal.connect(success_callback)
        self.success_signal = self.ComSuccess.myGUI_signal

        self.ComError = CommunicateError()
        self.ComError.myGUI_signal.connect(error_callback)
        self.error_signal = self.ComError.myGUI_signal

        self.calendar_days = calendar_days
        self.update_frequency = update_frequency
        self.kill = False

    def run(self):
        attempts = 0
        while True:
            try:
                cal = Calendar()
                appts_today = cal.get_calendar_appointments(start_days=0, days=1)
                appts_tomorrow = cal.get_calendar_appointments(start_days=1, days=1)
                appts_calendar = cal.get_calendar_appointments(start_days=0, days=self.calendar_days)
                self.success_signal.emit(self.calendar_days, appts_today, appts_tomorrow, appts_calendar)
                sleep(self.update_frequency)
                attempts = 0
            except Exception as e:
                attempts += 1
                if attempts > 5:
                    import traceback
                    print(traceback.format_exc())
                    self.error_signal.emit(e)
                    break


if __name__ == "__main__":
    print("Module test not implemented")
