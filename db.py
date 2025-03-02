import mysql.connector

def connect_db():
    try:
        db = mysql.connector.connect(
            host="mysql.gb.stackcp.com",  # Remove port from here
            port=63959,  # Specify port separately
            user="insta-auto-353038395f25",
            password="memahr27",
            database="insta-auto-353038395f25"
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
