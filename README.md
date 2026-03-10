AdNabu QA Assignment Automation
Project Description

This project contains automated test scripts for the AdNabuTestStore e-commerce platform.
The main scenario automated is: Search for a product and add it to the cart successfully using Python + Selenium + Pytest.

Project Structure
AdNabu_QA_Assignment/
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   └── product_page.py
│
├── tests/
│   └── test_add_to_cart.py
│
├── requirements.txt
└── README.md

pages/ → Contains Page Object Model (POM) classes

tests/ → Contains test scripts

requirements.txt → Lists all Python dependencies

README.md → Project documentation

Prerequisites

Python 3.9+

pip3

Google Chrome (latest stable version)

ChromeDriver matching your Chrome version, added to PATH

Setup Instructions

Clone the repository:

git clone https://github.com/naveensakthij/AdNabu_QA_Assignment.git
cd AdNabu_QA_Assignment

Install dependencies:

pip3 install -r requirements.txt
Running the Automated Test

Navigate to the project root folder:

cd /path/to/AdNabu_QA_Assignment

Run the test and generate HTML report:

pytest tests/test_add_to_cart.py --html=report.html

Open the HTML report in a browser:

open report.html
Test Scenario Details

Scenario: Search a product and add it to cart

Steps Automated:

Open the password-protected store page

Enter password: AdNabuQA and click Enter

Search for product: The Collection Snowboard

Click any product from search results

Click Add to Cart

Verify the product appears in the cart

Automation Features:

Uses Explicit Waits to avoid time.sleep() where possible

Page Object Model for clean and maintainable code

Generates HTML report using pytest-html

Notes / Tips

Make sure ChromeDriver version matches your installed Chrome browser version

Run tests from the project root folder to avoid ModuleNotFoundError

The script handles dynamic elements using Selenium Explicit Waits
