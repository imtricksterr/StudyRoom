# https://uconncalendar.lib.uconn.edu/reserve/GroupStudyRooms


# Adjusting in order to follow the UCONN IT policies on automation and web scraping.

from playwright.sync_api import sync_playwright

class Reservationist:

    playwright = sync_playwright().start()

    def main(self):
        """ Main function to run the reservation process """
        
        with sync_playwright() as p:
            self.student_schedule()
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("https://uconncalendar.lib.uconn.edu/reserve/GroupStudyRooms")




    def student_schedule(self):
        """ Takes students schedule for making reservations """ 
        day = input("Enter day you want a study room: ")
        start_time = input("What time do you want to start studying")
        end_time = input("What time do you want to stop studying")


    def find_selections(self):
        """ Uses student schedule to find reservations that work for them"""
        pass




    def submit_res(self):
        """ Uses student schedule to make selected reservations for the student"""
        pass