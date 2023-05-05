from selenium.webdriver.chrome.webdriver import WebDriver

from django.test import LiveServerTestCase

class Hosttest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = WebDriver("./other_files/cdriver/chromedriver/chromedriver")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_home_page(self):
        # self.driver.get(f"{self.live_server_url}/")
        self.driver.get('http://127.0.0.1:8000')
        self.driver.save_screenshot("./other_files/screenshots/image.png")
        page_title = "The install worked successfully! Congratulations!"
        assert page_title in self.driver.title