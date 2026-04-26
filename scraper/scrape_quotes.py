import csv
import time
import os

import undetected_chromedriver as uc

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():

    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = uc.Chrome(version_main=147, options=options)

    return driver


def extract_quotes(driver):

    wait = WebDriverWait(driver, 10)

    quotes = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "quote")
        )
    )

    data = []

    for q in quotes:
        try:
            text = q.find_element(By.CLASS_NAME, "text").text
            author = q.find_element(By.CLASS_NAME, "author").text

            data.append([text, author])

        except:
            continue

    return data


def save_to_csv(data):

    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", "complaints_db.csv")

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["review", "author"])

        for row in data:
            writer.writerow(row)

    print("File saved at:", file_path)


def main():

    url = "http://quotes.toscrape.com"

    driver = setup_driver()
    driver.get(url)

    all_data = []

    while True:

        time.sleep(2)

        data = extract_quotes(driver)
        all_data.extend(data)

        print(f"Collected so far: {len(all_data)}")

        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
            next_button.click()
        except:
            print("No more pages.")
            break

    save_to_csv(all_data)

    driver.quit()

if __name__ == "__main__":
    main()