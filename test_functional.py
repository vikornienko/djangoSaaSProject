import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from django.test import LiveServerTestCase

class Hosttest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = WebDriver("./other_files/cdriver/chromedriver/chromedriver")
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_home_page(self):
        # self.driver.get(f"{self.live_server_url}/")
        self.driver.get('http://127.0.0.1:8000')
        # time.sleep(2)
        self.driver.save_screenshot("./other_files/screenshots/image.png")
        # page_title = "The install worked successfully! Congratulations!"
        page_h1 = "Hello world!"

        # assert page_title in self.driver.title

        assert page_h1 in self.driver.find_element(By.TAG_NAME, "h1").text