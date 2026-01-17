from StudyRoom import Reservationist
from playwright.sync_api import sync_playwright
import re
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://uconncalendar.lib.uconn.edu/reserve/GroupStudyRooms")
    events = page.locator("a.fc-event")
    print(events.count())
    available = page.locator("a.fc-event:not(.fc-event-unavailable)")
    print(available.count())
    room_labels = page.locator("span.fc-cell-text")
    count = room_labels.count()
    print(count)


    ROOM_RE = re.compile(r"(?P<room>\w+)\s+(?P<capacity>\d+)\)")

    rooms = []
    for i in range(room_labels.count()):
        text = room_labels.nth(i).inner_text()
        match = ROOM_RE.search(text)

        if not match: continue

        room_name = match.group("room")
        capacity = int(match.group("capacity"))

        rooms.append({

            "room": room_name,
            "capacity": capacity,
            "row)index": i

        })
            

def eligible_rooms(rooms, group_size):
    return {
        room: info
        for room, info in rooms.items()
        if info["capacity"] >= group_size

    }