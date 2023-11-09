from time import sleep

from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome_options = Options()
# chrome_options.add_argument('--headless')

BASE_URL = "https://webscraper.io/"
LAPTOPS_URL = BASE_URL + "test-sites/e-commerce/more/computers/laptops"


def close_cookie_banner(driver: webdriver) -> webdriver:
    try:
        # Wait for the cookie banner to be present
        cookie_banner = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "closeCookieBanner"))
        )

        # Click on the close button to dismiss the banner
        cookie_banner.click()
    except Exception as e:
        print(f"Error closing cookie banner: {e}")
    finally:
        return driver


def handle_btn(driver: webdriver, url: str) -> webdriver:
    driver.get(url)
    driver = close_cookie_banner(driver)

    while True:
        try:
            more_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ecomerce-items-scroll-more"))
            )

            # Check if the element is visible
            if more_btn.is_displayed():
                more_btn.click()
            else:
                break
        except (ElementNotInteractableException, ElementClickInterceptedException):
            break

    return driver


if __name__ == "__main__":
    driver = webdriver.Chrome()  # options=chrome_options)
    handle_btn(driver, LAPTOPS_URL)

    # sleep(10)
    driver.quit()
