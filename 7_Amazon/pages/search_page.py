from selenium.webdriver.common.by import By


class SearchPage:
    """Search "samsung" text in search bar and go to the 2. Result page which is 3.one product click"""

    SEARCH_TEXTBOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT_BUTTON = (By.ID, "nav-search-submit-button")
    SEARCH_TEXT = "samsung"
    SEARCH_RESULT_LINK = (By.ID, 'search')
    SECOND_PAGE_BUTTON = (By.XPATH, "//li[@class = 'a-normal']//a[text() = '2']")
    PRODUCT_PAGE = (By.XPATH, "(//a[@class = 'a-link-normal a-text-normal'])[2]")

    def __init__(self, driver, methods):
        self.driver = driver
        self.methods = methods

    def enterSearchText(self):
        """
        Enter the search text to search bar

        """
        self.methods.wait_for_element(self.SEARCH_TEXTBOX).send_keys(self.SEARCH_TEXT)

    def clickSearch(self):
        """
        Click the search button for the text to search

        """
        self.methods.wait_for_element(self.SEARCH_SUBMIT_BUTTON).click()
        search_page_loaded = self.methods.element_exists(self.SEARCH_SUBMIT_BUTTON)
        assert search_page_loaded, True

    def clickSecondPage(self):
        """
        Go to the Second result page

        """
        self.methods.wait_for_element(self.SECOND_PAGE_BUTTON).click()
        second_page_loaded = self.methods.element_exists(self.SEARCH_RESULT_LINK)
        assert second_page_loaded, True

    def productClick(self):
        """
        Go to the Third one product page

        """
        self.methods.wait_for_element(self.PRODUCT_PAGE).click()
