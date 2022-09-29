from verint import *

from secrets import read_secrets
import time
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


# rooster = readVerint(verintURL, EMAIL, USERNAME, PASSWORD)
client = caldav.DAVClient(url=davURL, username=davUSER, password=davPASS)
my_principal = client.principal()
calendars = my_principal.calendars()
my_work_calendar = my_principal.calendar(name=work_calendar)

print(my_work_calendar)