from verint import *
from secrets import read_secrets

import caldav
from icalendar import Calendar, Event

import pytz
import locale
locale.setlocale(locale.LC_ALL, "nl_NL.utf8")
local = pytz.timezone("Europe/Amsterdam")

davURL = read_secrets()['davURL']
davUSER = read_secrets()['davUSER']
davPASS = read_secrets()['davPASS']
work_calendar = read_secrets()['work_calendar']
kantoor = read_secrets()['kantoor']
verintURL = read_secrets()['verintURL']
EMAIL = read_secrets()['budgetEMAIL']
USERNAME = read_secrets()['budgetUSER']
PASSWORD = read_secrets()['budgetPASS']
UID_ext = read_secrets()['UID_ext']

rooster = readVerint(verintURL, EMAIL, USERNAME, PASSWORD)

def time_to_utc(native):
    native = datetime.strptime(native, "%A %d %B %Y %H:%M")
    local_dt = local.localize(native, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    #utc_dt = utc_dt.strftime("%A %d %B %Y %H:%M")
    for r in (("-",""), (" ", "T"), (":", ""), ("+0000", "Z")):
    # for r in (("-",""), (" ", "T"), (":", "")):
        utc_dt = str(utc_dt).replace(*r)
    return utc_dt

def create_event(rooster):

    client = caldav.DAVClient(url=davURL, username=davUSER, password=davPASS)
    principal = client.principal()
    calendars = principal.calendars()
    my_work_calendar = principal.calendar(name=work_calendar)

    date = ""
    starttime = ""
    stoptime = ""
    comment = ""

    for day in rooster:
        date = day[0]
        starttime = day[1]
        stoptime = day[2]
        comment = day[3]

        location = kantoor
        DTSTAMP = str(datetime.now()).replace("-", "").replace(" ", "T").replace(":", "").split(".")[0] + "Z"
        DTSTART = time_to_utc(starttime)
        DTEND = time_to_utc(stoptime)
        UID = DTSTART + UID_ext


        ics = f"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Example Corp.//CalDAV Client//EN
BEGIN:VEVENT
UID:{UID}
DTSTAMP:{DTSTAMP}
DTSTART:{DTSTART}
DTEND:{DTEND}
LOCATION: {location}
SUMMARY:Werken
DESCRIPTION:{comment}
END:VEVENT
END:VCALENDAR
"""

       # ics += """END:VCALENDAR
       #     """

        # print(ics)
        my_event = my_work_calendar.save_event(ics)

if __name__ == "__main__":
    time.sleep(60)  # imagine you would like to start work in 1 minute first time
    while True:

        create_event(rooster)
        time.sleep(3600)  # do work every one hour
