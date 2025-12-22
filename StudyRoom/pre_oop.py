from playwright.sync_api import sync_playwright


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

# Step 3: Read availability table


# Step 4: Let user log in manually (pausing our Playwright session until done)
    print("Log in manually in order to continue.")
    page.pause()

# Step 5: Submitting reservation for user