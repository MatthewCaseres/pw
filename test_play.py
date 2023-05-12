import re
from playwright.sync_api import Page, expect
import datetime


def test_interest_rate_table(
    page: Page,
):
    # get the month of the current date in the format 01 for January, 02 for February, etc.
    month = datetime.datetime.now().strftime("%m")
    # and the year in the format 2021
    year = datetime.datetime.now().strftime("%Y")
    yield_curve_url = (
        "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month="
        + year
        + month
    )
    page.goto("https://playwright.dev/python/")
