"""
TODO:
"""

__author__ = "James Cook"
__copyright__ = "Copyright (C) 2021 James Cook"
__license__ = "GNU General Public License v3"
__version__ = "1.0.0"
__maintainer__ = "James Cook"
__email__ = "contact@cookjames.uk"

import pythoncom
import win32com.client
import datetime as dt


class Appointment:
    def __init__(self,
                 subject,
                 date,
                 start_time,
                 end_time,
                 organiser):
        self.subject = subject
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.organiser = organiser


class Calendar:

    def __init__(self):
        pass

    def get_calendar_appointments(self, start_days=0, days=14):
        """
        Get appointment details over the next X days in the future.
        """
        assert (days > 0)

        # setup outlook connection
        pythoncom.CoInitialize()
        Outlook = win32com.client.Dispatch("Outlook.Application")
        pythoncom.CoInitialize()
        ns = Outlook.GetNamespace("MAPI")

        # get appointments
        appts = ns.GetDefaultFolder(9).Items
        appts.Sort("[Start]")
        appts
        appts.IncludeRecurrences = True

        # set time restriction
        today = dt.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) + dt.timedelta(days=start_days)
        last_day = dt.timedelta(days=days) + today
        begin = today.date().strftime("%d/%m/%Y")
        end = last_day.date().strftime("%d/%m/%Y")
        restriction = "[Start] >= '" + begin + "' AND [End] <= '" + end + "'"
        appts = appts.Restrict(restriction)

        # put results into custom object
        return self._create_appointment_object(appts)

    def create_appointment(self, subject, start, duration_mins):
        pythoncom.CoInitialize()
        Outlook = win32com.client.Dispatch("Outlook.Application")
        pythoncom.CoInitialize()
        appt = Outlook.CreateItem(1)  # AppointmentItem
        appt.Start = start #"10/06/2021 23:50"  # dd/mm/YYYY hh:mm
        appt.Subject = subject
        appt.Duration = duration_mins  # In minutes (60 Minutes)
        appt.MeetingStatus = 1  # 1 - olMeeting; Changing the appointment to meeting. Only after changing the meeting status recipients can be added
        #appt.Recipients.Add("test@test.com")  # Don't end ; as delimiter
        appt.Save()
        #appt.Send()

    def _create_appointment_object(self, appts):
        """
        Creates Appointment objects for each appt in a list
        of appts from the Outlook client API.
        """
        appointments = []
        for a in appts:
            appointments.append(
                Appointment(
                    subject=a.Subject,
                    date=dt.datetime.strptime(str(a.Start)[:-6], '%Y-%m-%d %H:%M:%S'),
                    start_time=str(a.Start).replace("+00:00", "").split(" ")[1][:-3],
                    end_time=str(a.End).replace("+00:00", "").split(" ")[1][:-3],
                    organiser=a.Organizer))

        return appointments


if __name__ == "__main__":
    print("---- running module test -----")
    cal = Calendar()
    #cal.create_appointment(subject="TESTER", start="10/06/2021 23:50", duration_mins=5)
    appts = cal.get_calendar_appointments(1)

    for a in appts:
        print(a.subject)
        #print(a.date.strftime("%d/%m/%Y"))
        #print(a.start_time)
        #print(a.end_time)
        #print(a.organiser)