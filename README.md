# Instagram Automation Project

This project automates the process of creating and logging into Instagram accounts using Playwright and temporary email services.

#### Contributions are not welcomed!

## Project Structure

- `create_account.py`: Automates the creation of Instagram accounts.
- `login.py`: Automates the login process for Instagram accounts.
- `db.py`: Handles database connections and operations.
- `names.py`: Generates random names, usernames, and passwords.
- `tempemail.py`: Manages temporary email creation and retrieval of messages.
- `text.py`: Example script for using Playwright with Tor.

## Setup

1. **Install Dependencies**:
    ```sh
    pip install playwright playwright-stealth mysql-connector-python requests stem
    ```

2. **Set Up Database**:
    - Ensure you have a MySQL database running.
    - Update the database connection details in `db.py`.
    - Run the `create_table` function in `db.py` to create the necessary table.

3. **Run Playwright Install**:
    ```sh
    playwright install
    ```

## Usage

### Create Instagram Account

To create an Instagram account, run:
```sh
python create_account.py
```

### Login to Instagram Account

To login to an Instagram account, run:
```sh
python login.py
```

## Legal Disclaimer

This project is for educational purposes only. Automating the creation and login of Instagram accounts is against Instagram's [Terms of Use](https://help.instagram.com/581066165581870). Use of this project to violate Instagram's policies can result in the suspension or banning of your Instagram accounts. The author is not responsible for any misuse of this project.

## License

This project is licensed under the MIT License.