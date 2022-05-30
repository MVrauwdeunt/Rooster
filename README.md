# Rooster
Read closed source work schedule and add it to my Nextcloud using webdav

Since there is no easy way to view my work schedule and get the info in Homeassistant I wrote this script to copy the info to my Nextcloud calendar. The login consists of two parts. First you have to enter your email adres after submit you're redirected to another login page where you enter the provided username and password.


To login and read the source I used Selenium and Webdriver-Manager to create the event and upload this to my Nextcloud instance I use icalendar and webdav.

You can install these with the command
```pip install selenium webdriver-manager icalendar```