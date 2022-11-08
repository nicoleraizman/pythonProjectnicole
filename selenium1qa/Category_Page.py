from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Category_Page:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[class='productName ng-binding']")

    def pick_a_product(self,index):
        self.product()[index].click()


