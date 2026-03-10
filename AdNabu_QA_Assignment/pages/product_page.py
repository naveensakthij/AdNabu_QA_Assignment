from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductPage(BasePage):

    add_to_cart_button = (By.XPATH, "//button[contains(@id,'ProductSubmitButton')]")
    cart_icon = (By.ID, "cart-icon-bubble")
    cart_product_name = (By.CLASS_NAME, "cart-item__name")

    def add_product_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        )
        button.click()

    def open_cart(self):
        cart = self.wait.until(EC.element_to_be_clickable(self.cart_icon))
        self.driver.execute_script("arguments[0].click();", cart)

    def verify_product_in_cart(self):
        product = self.wait.until(
            EC.visibility_of_element_located(self.cart_product_name)
        )
        return product.text
