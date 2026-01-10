from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://uconncalendar.lib.uconn.edu/reserve/GroupStudyRooms")
    events = page.locator("a.fc-event")
    print(events.count())
    available = page.locator("a.fc-event:not(.fc-event-unavailable)")
    print(available.count())