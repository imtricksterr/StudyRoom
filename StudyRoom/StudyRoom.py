# https://uconncalendar.lib.uconn.edu/reserve/GroupStudyRooms


# Adjusting in order to follow the UCONN IT policies on automation and web scraping.

from playwright.sync_api, import sync_playwright

class Reservationist:


    def main(self):
       """ Main function to run the reservation process """
        with sync_playwright() as p:
            browser = p.chromium.launch()



    def student_schedule(self):
        """ Takes students schedule for making reservations """ 
        pass




    def find_selections(self):
        """ Uses student schedule to find reservations that work for them"""
        pass




    def submit_res(self):
        """ Uses student schedule to make selected reservations for the student"""
        pass