from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from components.bee_movie import bee_movie_spam
import random


class chrome_driver:
    def __init__(self, chromedriver):
        self.driver = chromedriver

    def exec(self, url):
        stealth(
            self.driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Darwin",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        self.driver.get(url)
        return self.driver

    def run(self):
        self.exec(
            "https://docs.google.com/forms/d/e/1FAIpQLSe5F9dc_5XYTOdG-bil06OYFaUaMmEqJuQEAYrMk9rNWQUwow/viewform"
        )

        click = self.driver.find_element(By.ID, "i5")
        click2 = self.driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
        )
        field = self.driver.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
        self.driver.implicitly_wait(2)
        click.click()
        bee = bee_movie_spam()
        matrix = bee.read_lines()
        selected_value = random.choice(matrix)
        field.send_keys(selected_value)
        click2.click()
