import unittest

from base.base_page import BaseClass
from pages.login_page import LoginPage
from pages.main_page import AMAZON
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from selenium import webdriver


class Amazon(unittest.TestCase):
    """ Test case is:
        1. Go http://www.amazon.com and confirm
        2. Open the login page and log-in with your account
        3. Type 'samsung' to the search box and click to the search button
        4. Confirm that there are results for 'samsung'
        5. Go second page of the search page and confirm that it is the second page
        6. Click on the third product of the top and click 'Add to List' button
        7. Click on the "View Your List" where is the top of the page
        8. Confirm that the same product is added from previous page
        9. Delete this product from wishlist page by clicking 'Delete item' button
        10. Confirm that this product no longer on the wishlist

    """

    def setUp(self):
        """Selenium initializing requirements are met in here."""

        self.driver = webdriver.Chrome("C:/Users/fadime.ozdemir/Documents/chromedriver_win32/chromedriver.exe")
        self.driver.maximize_window()
        self.methods = BaseClass(self.driver)
        self.main = AMAZON(self.driver, self.methods)
        self.login = LoginPage(self.driver, self.methods)
        self.search = SearchPage(self.driver, self.methods)
        self.product = ProductPage(self.driver, self.methods)

    def test_amazon(self):
        self.main.navigate_to_home_page()
        self.login.navigate_to_login_page()
        self.login.login_info_filling()
        self.login.login()
        self.search.enterSearchText()
        self.search.clickSearch()
        self.search.clickSecondPage()
        self.search.productClick()
        self.product.addToList()
        self.product.viewList()
        self.product.deleteItem()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
