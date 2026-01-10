from playwright.sync_api import sync_playwright
from collections import defaultdict

# screen of cells on website are divs
# cell elements are labelled: <div class= "fc-event-title-contianer"> == $0


# if size < 6: 
    # rooms = 1103A, 1103B, 1104A, 1104B, 1104C, 1104D, 1104E, 1104F, 1105A, 1105B, 1106A, 1106B, 1128 

# if size > 6:
    # rooms = 2200, 2149

# else: 
    # rooms = 2100, 2149, 2177, 4100, 4129, 4134A, 4134B, 4177, 4182A, 4182B, 4200, B141A, B141B, B144A, B144B, B149A, B149B





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
    events = page.locator("a.fc-event") # changed this so i know the gaps?
    slots = []
    # pass this to method that compares available slots to student schedule

    for i in range(events.count()):
        e = events.nth(i)

        classes = e.get_attribute("class") or ""
        available = "fc-event-unavailable" not in classes

        slots.append({

            "room": e.get_attribute("data-resource-id"),
            "start": e.get_attribute("data-start"),
            "end": e.get_attribute("data-end"),
            "available": available,
            "element": e

        })


    rooms = defaultdict(list)

    for slot in slots:
        rooms[slot["room"]].append(slot)


    for room_slots in rooms.values():
        room_slots.sort(key=lambda s: s["start"])



    # Step 4: Grouping available slots (might have to do the graph)
    def group_available_runs(slots):
        runs = []
        current = []

        for slot in slots:
            if slot["available"]:
                current.append(slot)
            
            else:
                if current:
                    runs.append(current)
                    current = []


        if current:
            runs.append(current)

        return runs




#for room_id, room slots in rooms.items():
    #runs = group_available_runs(room_slots)

    #for run in runs:
        #print(room_id, run[0]["start"], "→", run[-1]["end"])




    """  
    <a class = "fc-event"
    data-start = "2026-01-09T15:00:00"   leaving this here for reference
    data-end = "2026-01-09T15:30:00"
    
    """

    


# Step 4: Check if availability table matches user defined schedule at all; anticipating the logic for this will be a pain
def run_covers_request(run, desired_start, desired_end):
    run[0]["start"] <= desired_start and run[-1]["end"] >= desired_end



# Step 5: Return available study room sessions that work for the student
    # return study rooms available to user

    # have user pick one study room and send that to booking method; repetitive, but am not confident atm that i can figure out how to do multiple bookings in one session


def find_matching_runs(rooms, desired_start, desired_end):

    matches = []

    for room_id, room_slots in rooms.items():
        runs = group_available_runs(room_slots)

        for run in runs:
            if run_covers_request(run, desired_start, desired_end):
                matches.append({
                    "room": room_id,
                    "start": run[0]["start"],
                    "end": run[-1]["end"],
                    "run": run
                })

    return matches



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
