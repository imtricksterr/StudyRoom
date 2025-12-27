from playwright.sync_api import sync_playwright


# screen of cells on website are divs
# cell elements are labelled: <div class= "fc-event-title-contianer"> == $0



# Step 0: Ask user their preferred days of study, time window, and room size preference
def get_student_schedule():
    return {
        "day": input("Day: "),
        "start": input("Enter desired start time: "),
        "end": input("Enter desired end time:"),
        "size": input("Enter desired room size:")

    }

# Step 1: Start Chromium session in headed mode (allows us to see what is occurring)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

# Step 2: Open Reservations Page
    page = browser.new_page
    page.goto("https://uconncalendar.lib.uconn.edu/reserve/GroupStudyRooms")
    page.pause()

# Step 3: Read availability table
    available_slots = page.locator("div.fc-event:not(.fc-event-unavailable)")
    # pass this to method that compares available slots to student schedule

# Step 4: Check if availability table matches user defined schedule at all; anticipating the logic for this will be a pain
    # if user schedule matches an open study room:
    # add study room to dict

    #else (user cannot get a study room that matches their schedule):
    # print to user that there are no bookings that work for them


# Step 4.5: Helper function that just holds a dictionary of study room: time
    # could try implementing a triple dictionary in order to store study room: start time: end time


# Step 5: Return available study room sessions that work for the student
    # return study rooms available to user

    # have user pick one study room and send that to booking method; repetitive, but am not confident atm that i can figure out how to do multiple bookings in one session



# Step 6: Let student pick specific study room
    # have user pick one study room and send that to booking method; repetitive, but am not confident atm that i can figure out how to do multiple bookings in one session



# Step 7: proceed with booking process
    # booking script until authentication section



# Step 8: Let user log in manually (pausing our Playwright session until done)
    page.pause()
    print("Log in manually in order to continue.")
    page.wait_for_url("https://uconncalendar.lib.uconn.edu/spaces/auth?returnUrl=%2Freserve%2FGroupStudyRooms") 
    print("Detected Login, booking your study room...")

# Step 9: Finish submitting reservation for user after authentication
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Submit my Booking").click()
