import random
import json
import time
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

from db import  connect_db
from names import generate_full_name, gen_password, gen_username
from tempemail import generate_email, get_messages


# Webshare.io Proxy Config
# PROXY_SERVER = "socks5://xyapizye-rotate:xxi1nxa8jdfc@p.webshare.io:80"

# User-Agent List for Fingerprint Spoofing
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:119.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Linux; Android 11; Mobile; rv:118.0) Gecko/20100101 Firefox/118.0"
]

# Human-like Mouse Movement
def move_mouse_randomly(page):
    for _ in range(random.randint(5, 10)):
        x = random.randint(100, 900)
        y = random.randint(100, 600)
        page.mouse.move(x, y, random.uniform(0.1, 0.5))
        time.sleep(random.uniform(0.2, 0.5))

# Human-like Typing
def fill_input_with_cursor(page, selector, text):
    page.wait_for_selector(selector)
    page.mouse.move(random.randint(100, 500), random.randint(100, 500))
    page.click(selector)
    for char in text:
        page.keyboard.type(char, delay=random.uniform(50, 200))

# Automate Instagram Signup
def create_instagram_account():
    with sync_playwright() as p:
        try:
            # Launch browser with proxy
            browser = p.firefox.launch(
                headless=False,
                proxy={"server": "socks5://p.webshare.io:80",
                       "username": "xyapizye-rotate",
                       "password": "xxi1nxa8jdfc"}
            )
            context = browser.new_context(
                user_agent=random.choice(USER_AGENTS),
                viewport={"width": random.randint(1280, 1920), "height": random.randint(720, 1080)},
                java_script_enabled=True,
                bypass_csp=True
            )
            
            page = context.new_page()
            stealth_sync(page)  # Apply stealth mode

            # Generate random details
            fullname = generate_full_name()
            username = gen_username()
            password = gen_password()
            email_address = generate_email(username)

            if not email_address:
                print("Failed to get email. Exiting...")
                return

            page.goto("https://www.instagram.com/accounts/emailsignup/", timeout=60000)
            time.sleep(random.uniform(3, 6))

            # Fill Sign-up Form
            fill_input_with_cursor(page, "input[name='emailOrPhone']", email_address)
            fill_input_with_cursor(page, "input[name='password']", password)
            fill_input_with_cursor(page, "input[name='fullName']", fullname)
            fill_input_with_cursor(page, "input[name='username']", username)

            time.sleep(random.uniform(2, 5))
            move_mouse_randomly(page)

            # Click Sign Up
            page.click("button[type='submit']")
            time.sleep(5)

            # Select Birthdate
            page.wait_for_selector("select[title='Month:']")
            random_day = str(random.randint(1, 28))
            random_year = str(random.randint(1985, 2005))
            page.select_option("select[title='Day:']", random_day)
            page.select_option("select[title='Year:']", random_year)

            time.sleep(5)
            move_mouse_randomly(page)
            page.click("button[type='button']")

            # Email Confirmation
            time.sleep(10)
            move_mouse_randomly(page)

            # Get Confirmation Code
            code = get_messages(email_address)
            page.wait_for_selector("input[name='email_confirmation_code']", timeout=10000)
            fill_input_with_cursor(page, "input[name='email_confirmation_code']", code)
            page.click('text=Next')

            time.sleep(random.uniform(5, 15))
            move_mouse_randomly(page)

            # Capture Session Token
            cookies = context.cookies()
            session_token = json.dumps(cookies)

            # Save to Database
            db = connect_db()
            if db:
                cursor = db.cursor()
                cursor.execute("INSERT INTO accounts (username, password, email, session_token) VALUES (%s, %s, %s, %s)",
                               (username, password, email_address, session_token))
                db.commit()
                db.close()

            print(f"Account Created: {username} | {password}")

        except Exception as e:
            print(f"Error during account creation: {e}")
        finally:
            browser.close()

# Main Execution
if __name__ == "__main__":
   create_instagram_account()