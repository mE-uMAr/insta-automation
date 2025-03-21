import requests
import json
import os
import re

EMAILS_FILE = "emails.json"
API_BASE = "https://api.tm"

def save_email(email, password):
    data = {"email": email, "password": password}
    if os.path.exists(EMAILS_FILE):
        with open(EMAILS_FILE, "r") as f:
            try:
                emails = json.load(f)
            except json.JSONDecodeError:
                emails = []
    else:
        emails = []

    emails.append(data)
    
    with open(EMAILS_FILE, "w") as f:
        json.dump(emails, f, indent=4)

def generate_email(username):
    url = f"{API_BASE}/accounts"
    domain = requests.get(f"{API_BASE}/domains").json()["hydra:member"][0]["domain"]
    email = f"{username}@{domain}"
    password = "securepassword123"

    payload = {"address": email, "password": password}
    response = requests.post(url, json=payload)

    if response.status_code == 201:
        print(f"Created Email: {email}")
        save_email(email, password)

        return email
    else:
        print(f"Failed to create temp email: {response.text}")
        return

def get_messages(email):
    with open(EMAILS_FILE, "r") as f:
        emails = json.load(f)

    account = next((acc for acc in emails if acc["email"] == email), None)
    if not account:
        print("Email not found.")
        return

    token_resp = requests.post(f"{API_BASE}/token", json={"address": email, "password": account["password"]})
    if token_resp.status_code != 200:
        print("Failed to authenticate.")
        return
    
    token = token_resp.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    messages_resp = requests.get(f"{API_BASE}/messages", headers=headers)

    if messages_resp.status_code == 200:
        messages = messages_resp.json()["hydra:member"]
        if messages:
            for msg in messages:
                code = re.search(r"\d{6}", msg['subject'])
                # print(f"code in msg : {repr(msg['intro'])}")
                if code:
                    print(f"code received: {code.group()}")
                    return f"{code.group()}"
        else:
            print("No new messages.")
    else:
        print("Failed to retrieve messages.")
