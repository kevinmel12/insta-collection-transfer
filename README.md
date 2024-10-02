# Instagram Automation Script

This project is a Python script that uses **Selenium** to automate the login process for two Instagram accounts, extract saved post links from the first account, and save them to the second account.

## Features

- Automatic login to Instagram with two accounts.
- Extraction of saved post links from one account's saved collection.
- Automatic saving of the posts to another Instagram account.
- Automatic handling of Instagram's cookie pop-ups.

## Prerequisites

- **Python**
- **Google Chrome**
- **Selenium WebDriver** for Chrome
- **Webdriver Manager**
- A `.env` file to store Instagram credentials.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/kevinmel12/insta-collection-transfer.git
    ```

2. **Install dependencies:**
    Make sure you're in the project directory, then run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the credentials in the `.env` file:**

   Create a `.env` file at the root of the project and follow the model of the `env_sample` file:
    ```
    ACCOUNT1_USERNAME={FIRST_ACCOUNT_USERNAME}
    ACCOUNT1_PASSWORD={FIRST_ACCOUNT_PASSWORD}
    ACCOUNT2_USERNAME={SECOND_ACCOUNT_USERNAME}
    ACCOUNT2_PASSWORD={SECOND_ACCOUNT_PASSWORD}
    SOURCE_COLLECTION_URL={FIRST_ACCOUNT_COLLECTION_LINK}
    ```

## Usage

1. **Run the script:**
   Execute the following command to start the script:
    ```bash
    python script.py
    ```

2. **Login to the first Instagram account:**

   The script automatically logs into the first Instagram account using the credentials provided in the `.env` file. It then opens the saved posts collection page at the following URL:

    ```python
    saves_url = f"https://www.instagram.com/{username}/saved/_/*************/"
    ```
    Here, `{username}` is replaced by the first account's username (defined in the `.env` file under `ACCOUNT1_USERNAME`).

3. **Extract saved post links:**

   The script scrolls through the collection page to load all the saved posts and extracts the post links using XPATH. The links are then saved to the `instagram_links.txt` file.

4. **Login to the second Instagram account:**

   After extracting the links, the script logs into the second Instagram account using the credentials provided in the `.env` file. It opens each previously saved link in a new window and attempts to save them to the second account's collection.

   The collection URL for the second account looks like this:
    ```python
    saves_url = f"https://www.instagram.com/{username}/saved/_/*************/"
    ```
    Here, `{username}` is replaced by the second account's username (defined in the `.env` file under `ACCOUNT2_USERNAME`).

## Dependencies

- **Selenium**: Library to control the browser.
- **Webdriver Manager**: To automatically install and manage Chrome WebDriver.
- **BeautifulSoup**: For data scraping (if needed for future features).
- **Requests**: For making HTTP requests.

## Notes

- Ensure that both Chrome and its WebDriver are up to date to avoid compatibility issues.
- Modify the `XPATH` in the script if Instagram updates its HTML structure.