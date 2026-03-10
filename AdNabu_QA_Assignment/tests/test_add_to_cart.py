import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from selenium import webdriver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup Chrome
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_add_to_cart(driver):
    home = HomePage(driver)
    product = ProductPage(driver)

    # Open store and login
    home.open_store()
    home.login("AdNabuQA")

    # Search product
    home.search_product("snowboard")

    # Select product
    home.select_product()

    # Add product to cart
    product.add_product_to_cart()

    # Open cart and verify
    product.open_cart()
    product_name = product.verify_product_in_cart()
    assert product_name is not None, "Product was not added to cart"
    print("Product added to cart:", product_name)
