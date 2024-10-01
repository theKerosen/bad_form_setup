from components.driver import chrome_driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random


class main:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-gpu")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.service = Service()
        self.chrome = webdriver.Chrome(service=self.service, options=self.options)
        self.counter = 0

    def run(self):
        thing = chrome_driver(self.chrome)
        thing.exec(
            "https://docs.google.com/forms/d/e/1FAIpQLSe5F9dc_5XYTOdG-bil06OYFaUaMmEqJuQEAYrMk9rNWQUwow/viewform"
        )

        while True:
            thing.run()
            self.counter += 1
            print(self.counter)
            time.sleep(0.5)


if __name__ == "__main__":
    main().run()
