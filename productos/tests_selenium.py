from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import unittest

class ProductoSeleniumTest(unittest.TestCase):

    def setUp(self):
        service = Service('./drivers/chromedriver.exe')  # ruta a tu driver
        self.driver = webdriver.Chrome(service=service)

    def test_open_homepage(self):
        self.driver.get("http://127.0.0.1:8000/")  # ajusta la URL si es necesario
        time.sleep(2)
        self.assertIn("The install worked successfully", self.driver.title)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
