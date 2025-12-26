from playwright.sync_api import sync_playwright


# screen of cells on website are divs
# cell elements are labelled: <div class= "fc-event-title-contianer"> == $0



# Step 0: Ask user their preferred days of study, time window, and room size preference
def get_student_schedule():
    return {
        "day": input("Day: "),
        "start": input("Start time: "),
        "end": input("end time:")

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

# Step 4: Check if availability table matches user defined schedule; anticipating the logic for this will be a pain

# if user schedule matches an open study room:
# add study room to dict
# return study rooms available to user
# have user pick one study room and send that to booking method; repetitive, but am not confident atm that i can figure out how to do multiple bookings in one session

#else (user cannot get a study room that matches their schedule):
# print to user that there are no bookings that work for them

# i should separate these into different methods im realizing, so ill be sure to do that tomorrow


# Step 5: Let user log in manually (pausing our Playwright session until done)
    page.pause()
    print("Log in manually in order to continue.")
    page.wait_for_url("https://uconncalendar.lib.uconn.edu/spaces/auth?returnUrl=%2Freserve%2FGroupStudyRooms") 

    
# Step 6: Submitting reservation for user
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Submit my Booking").click()
