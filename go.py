from playwright.sync_api import sync_playwright
import datetime

# get the month of the current date in the format 01 for January, 02 for February, etc.
month = datetime.datetime.now().strftime("%m")
# and the year in the format 2021
year = datetime.datetime.now().strftime("%Y")
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    # we are going to get the daily treasury par yield curve
    page.goto("http://playwright.dev")
    print(page.title())
    browser.close()
