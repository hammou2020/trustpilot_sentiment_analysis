"""
Common settings used in the scraping scripts.
"""

import os

from selenium.webdriver.chrome.options import Options

# This is the root for our scraping folder
BASE_DIR = os.path.dirname(__file__)

# This is where we'll start our app from
BASE_URL = "https://trustpilot.com"

# This is how our chrome browser will run
CHROME_OPTIONS = Options()
# Rendering a browser graphically is computationally expensive, and kind of annoying (pops over stuff), so we'll use a
# "headless" browser, which will just run in the background, instead of appearing as a new window. If you want to see
# the browser work, remove this option.
# CHROME_OPTIONS.add_argument("--headless")
CHROME_OPTIONS.add_argument("start-maximized")
# CHROME_OPTIONS.add_argument("--kiosk")

# This is used by the webdriver to determine how long it will wait for an element to appear while a page is loading
MAX_PAGE_LOAD_TIME = 0.1

# Set this to however many reviews there are to a page
REVIEWS_PER_PAGE = 20
