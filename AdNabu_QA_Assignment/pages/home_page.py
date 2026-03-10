from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):

    password_field = (By.ID, "password")
    login_button = (By.XPATH, "//button[@type='submit']")

    search_icon = (By.CLASS_NAME, "modal__toggle-open")
    search_box = (By.ID, "Search-In-Modal")

    product_link = (By.XPATH, "//a[contains(@id,'CardLink--')]")

    def open_store(self):
        self.driver.get("https://adnabu-store-assignment1.myshopify.com/password")

    def login(self, password):
        self.wait_for_element(self.password_field).send_keys(password)
        self.click_element(self.login_button)

    def search_product(self, product):
        self.click_element(self.search_icon)
        element = self.wait_for_element(self.search_box)
        element.send_keys(product)
        element.submit()  # press enter to search

    def select_product(self):
        # Wait for search result product card
        product = self.wait.until(
            EC.element_to_be_clickable(self.product_link)
        )
        # Click via JavaScript to avoid intercept issues
        self.driver.execute_script("arguments[0].click();", product)
