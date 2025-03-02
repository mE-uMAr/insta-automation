import random
import time
from playwright.sync_api import sync_playwright
from db import FetchAccounts, update_session_id
import json

def login_account():
    accounts = FetchAccounts().get_all_accounts()
    if not accounts:
        print("No accounts found in the database.")
        return
    
    for email, username, password, session_token in accounts:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=100)
            context = browser.new_context()
            
            if session_token:
                print(f"Trying session login for: {email}")
                cookie = json.loads(session_token)
                context.add_cookies(cookie)
                page = context.new_page()
                page.goto(f"https://www.instagram.com/{username}/", timeout=60000)
                time.sleep(5)
                if page.url == f"https://www.instagram.com/{username}/":
                    print(f"Successfully logged in using session ID: {email}")
                    
                    time.sleep(60)
                    browser.close()
                    continue
                else:
                    print(f"Session login failed for {email}. Trying manual login...")
            
            # Manual login
            try:
                page = context.new_page()
                page.goto("https://www.instagram.com/accounts/login/", timeout=60000)
                time.sleep(3)
                page.fill("input[name='username']", email)
                page.fill("input[name='password']", password)
                time.sleep(random.uniform(2, 5))
                page.click("button[type='submit']")
                time.sleep(5)
                
                if "/accounts/onetap" in page.url or "instagram.com" in page.url:
                    print(f"Successfully logged in manually: {email}")
                    
                    # Save new session ID
                    update_session_id(email, json.dumps(context.cookies()))


                    time.sleep(60)
                else:
                    print(f"Manual login failed for {email}")
                
            except Exception as e:
                print(f"Error during manual login for {email}: {e}")
            finally:
                browser.close()

if __name__ == "__main__":
    login_account()
