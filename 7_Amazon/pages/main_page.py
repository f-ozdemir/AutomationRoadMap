from selenium.webdriver.common.by import By


class AMAZON:
    """AMAZON class lands in the website and it has all the navigation functions"""

    website = "https://www.amazon.com.tr/"
    MAIN_PAGE = (By.ID, "nav-logo-sprites")

    def __init__(self, driver, methods):
        self.driver = driver
        self.methods = methods

    def navigate_to_home_page(self):
        """
        Navigates to the homepage and checks it

        """
        self.driver.get(self.website)
        self.methods.wait_for_element(self.MAIN_PAGE).click()
        home_page_loaded = self.methods.element_exists(self.MAIN_PAGE)
        assert home_page_loaded, True
