from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# import re
from secrets import read_secrets
from datetime import datetime
from datetime import date
import time
import locale
locale.setlocale(locale.LC_ALL, "nl_NL.utf8")

verintURL = read_secrets()['verintURL']
EMAIL = read_secrets()['budgetEMAIL']
USERNAME = read_secrets()['budgetUSER']
PASSWORD = read_secrets()['budgetPASS']


def find_between( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def readVerint(URL, EMAIL, USERNAME, PASSWORD):
    #object of Options class
    options = webdriver.ChromeOptions()
    # WebDriverManager.chromedriver().driverVersion("101.0.4951.64").setup();
    #add user Agent
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    +"AppleWebKit/537.36 (KHTML, like Gecko)"
    +"Chrome/87.0.4280.141 Safari/537.36")
    options.add_argument("--enable-javascript")
    # DRIVER_PATH = "/home/zanbee/Downloads/chromedriver"
    DRIVER_PATH = "/usr/bin/chromedriver"

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(URL)
    
    login = driver.find_element(By.NAME, "username").send_keys(EMAIL)
    submit = driver.find_element(By.XPATH, '//div[@class="loginButton"]').click()
    user = driver.find_element(By.NAME, "UserName").send_keys(USERNAME)
    password = driver.find_element(By.NAME, "Password").send_keys(PASSWORD)
    submit = driver.find_element(By.XPATH, '//span[@id="submitButton"]').click()

    time.sleep(16) #wait 10 seconds
    # frame = driver.find_element(By.XPATH, '//*[@id="mctnt"]')
    driver.switch_to.frame('mctnt')
    time.sleep(10) #wait 10 seconds
<<<<<<< HEAD
#    frame = driver.find_element(By.XPATH, '//*[@id="mctnt"]')
    driver.switch_to.frame('mctnt')
    time.sleep(10) #wait 10 seconds
=======
>>>>>>> 7dda4e0898da04ab9ab1bc9bde7d88181731766e
    select = driver.find_element(By.XPATH, '//*[@id="_drpOBTWrapper_img_id"]').click()

    select = driver.find_element(By.XPATH, '//*[@id="_drp_BTN_5"]').click()

    source = driver.page_source
    days = source.strip()
    days = source.split("<th ")

    result = []
    for day in days:
        if day and '<span class="shift-date">' in day:
            if '<span class="shift-label">vrij</span>' not in day and 'afwezig' not in day:
                a = []

                str(datetime.now()).replace("-", "").replace(" ", "T").replace(":", "").split(".")[0] + "Z"

                timeblock = find_between(day, '<span class="shift-label">', '</span>')
                shiftdate = find_between(day, '<span class="shift-date">', '</span>')
                formated_date = datetime.strptime(shiftdate, '%A %d %B %Y')
                formated_date = formated_date.strftime('%Y-%m-%d')
                formatted_date = time.strptime(formated_date, "%Y-%m-%d")
                timeblock = timeblock.split(" - ")
                starttime = shiftdate+ " " + timeblock[0]
                stoptime = shiftdate + " " + timeblock[1]
                today = date.today()
                formatted_date = datetime.strptime(formated_date, "%Y-%m-%d").date()
                activities = find_between(day, " Activiteiten ", " Location " )

                block = ""
                if formatted_date > today:
                    a.append(shiftdate)
                    activities = activities.split('<table class="w100 activity-event">')
                    for event in activities:
                        if event:
                            if block:
                                block += "\\n"
                            event_time = find_between(event, '<td class="activity-event-period" style="left-padding:3px; ">', '</td>' )
                            event_item = find_between(event, '<td class="w150px activity-event-activity"> &nbsp;', '_3107328&nbsp;</td>' )
                            block += event_time + " " + event_item

                    a.append(starttime)
                    a.append(stoptime)
                    a.append(block)
                
                if a:
                    result.append(a)

<<<<<<< HEAD
#    driver.save_screenshot('screenshot.png')
#    print(result)
=======
    # driver.save_screenshot('screenshot.png')
    # print(result)
>>>>>>> 7dda4e0898da04ab9ab1bc9bde7d88181731766e
    driver.quit()
    return result