from playwright.sync_api import sync_playwright
import stem
from stem.control import Controller
import time

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False,proxy={"server": "socks5://127.0.0.1:9050"})
    page = browser.new_page()
    page.goto("http://check.torproject.org")
    page.goto("http://whatismyipaddress.com",timeout=60000)
    time.sleep(600)
    print(page.title())
    browser.close()

with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    controller.signal(stem.Signal.NEWNYM)
