from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page()
    page.goto("https://uconncalendar.lib.uconn.edu/reserve/GroupStudyRooms")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Submit my Booking").click()
    
