import mysql.connector

def connect_db():
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",  # Remove port from here
            port=3306,  # Specify port separately
            user="root",
            password="memahr27",
            database="insta_auto"
        )
        print("Connected to DB successfully")
        return db
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None

def create_table():
    db = connect_db()
    if db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255),
                password VARCHAR(255),
                email VARCHAR(255),
                session_token TEXT
            )
        """)
        print("created table in db")
        db.commit()
        db.close()


def update_session_id(email, new_session_id):
    try:
        db = connect_db()
        cursor = db.cursor()
        
        query = "UPDATE accounts SET session_token = %s WHERE email = %s"
        cursor.execute(query, (new_session_id, email))
        
        db.commit()
        print(f"Session ID updated for {email}")

        cursor.close()
        db.close()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")



# def fetch_accounts():
#     db = connect_db()
#     if db:
#         cursor = db.cursor()
#         cursor.execute("SELECT email, username, password FROM accounts")
#         accounts = cursor.fetchall()
#         db.close()
        
#         return accounts
    
class FetchAccounts:
    def __init__(self):
        self.accounts = []
        db = connect_db()
        if db:
            cursor = db.cursor()
            cursor.execute("SELECT email, username, password, session_token FROM accounts")
            self.accounts = cursor.fetchall()  # Fetch all rows as a list of tuples
            db.close()

    def get_all_accounts(self):
        return self.accounts  # Returns a list of (email, username, password)

    def get_first_account(self):
        return self.accounts[0] if self.accounts else None 


# db = connect_db()
# if db:
#     cursor = db.cursor()
#     cursor.execute("INSERT INTO accounts (username, password, email, session_token) VALUES (%s, %s, %s, %s)",
#                                ("willa97cy0v", "XEi%E2#zra%K", "willa97cy0v@edny.net", '[{"name": "csrftoken", "value": "asdfghjklnbvcxz", "domain": ".instagram.com", "path": "/", "expires": 1772300099.313685, "httpOnly": false, "secure": true, "sameSite": "Lax"}, {"name": "datr", "value": "JUXDZ1DM9O7tWRN_HoK_IjMk", "domain": ".instagram.com", "path": "/", "expires": 1775410469.185689, "httpOnly": true, "secure": true, "sameSite": "None"}, {"name": "ig_did", "value": "AD892BEB-64D5-46A0-9234-067F91FB8E3E", "domain": ".instagram.com", "path": "/", "expires": 1772386469.185859, "httpOnly": true, "secure": true, "sameSite": "None"}, {"name": "wd", "value": "1280x720", "domain": ".instagram.com", "path": "/", "expires": 1741455288, "httpOnly": false, "secure": true, "sameSite": "Lax"}, {"name": "dpr", "value": "1.0000000298023224", "domain": ".instagram.com", "path": "/", "expires": 1741455299, "httpOnly": false, "secure": true, "sameSite": "None"}, {"name": "mid", "value": "Z8NFJgALAAE0sEKXvb_zlECH3mrl", "domain": ".instagram.com", "path": "/", "expires": 1775410476, "httpOnly": false, "secure": true, "sameSite": "Lax"}, {"name": "ps_l", "value": "1", "domain": ".instagram.com", "path": "/", "expires": 1775410486.765596, "httpOnly": true, "secure": true, "sameSite": "Lax"}, {"name": "ps_n", "value": "1", "domain": ".instagram.com", "path": "/", "expires": 1775410486.766051, "httpOnly": true, "secure": true, "sameSite": "None"}, {"name": "ig_nrcb", "value": "1", "domain": ".instagram.com", "path": "/", "expires": 1772386489.410511, "httpOnly": false, "secure": true, "sameSite": "Lax"}, {"name": "sessionid", "value": "72673196230%3AfgtjnbhVOgDuHH%3A17%3AAYfy9Wlx-VpJAIFqsiPte3T62UDt9brm_0u5aCkqiw", "domain": ".instagram.com", "path": "/", "expires": 1772386499.313, "httpOnly": true, "secure": true, "sameSite": "Lax"}, {"name": "ds_user_id", "value": "72673196230", "domain": ".instagram.com", "path": "/", "expires": 1748626499.31348, "httpOnly": false, "secure": true, "sameSite": "Lax"}]'))
#     db.commit()
#     db.close()